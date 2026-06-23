from flask import Flask, render_template

from database import (
    initialize_database,
    get_logs,
    get_alerts,
    clear_logs,
    clear_alerts
)

from collector import collect_windows_logs
from detector import detect_threats


app = Flask(__name__)


# -------------------------
# Dashboard
# -------------------------

@app.route("/")
def dashboard():


    # Collect latest Windows logs
    collect_windows_logs()


    # Get logs after collection
    logs = get_logs()


    # Run detection engine
    detect_threats(logs)


    alerts = get_alerts()



    total_logs = len(logs)

    total_alerts = len(alerts)


    users = len(
        set(
            log["username"]
            for log in logs
        )
    )


    sources = len(
        set(
            log["source"]
            for log in logs
        )
    )



    return render_template(
        "dashboard.html",
        logs=logs,
        alerts=alerts,
        total_logs=total_logs,
        total_alerts=total_alerts,
        users=users,
        sources=sources
    )



# -------------------------
# Logs Page
# -------------------------

@app.route("/logs")
def logs_page():


    logs = get_logs()


    return render_template(
        "logs.html",
        logs=logs
    )



# -------------------------
# Alerts Page
# -------------------------

@app.route("/alerts")
def alerts_page():


    alerts = get_alerts()


    return render_template(
        "alerts.html",
        alerts=alerts
    )



# -------------------------
# Analytics Page
# -------------------------

@app.route("/analytics")
def analytics_page():


    logs = get_logs()

    alerts = get_alerts()


    return render_template(
        "analytics.html",
        logs=logs,
        alerts=alerts
    )



# -------------------------
# Start Application
# -------------------------

if __name__ == "__main__":


    initialize_database()


    # Remove old demo data only once
    clear_logs()
    clear_alerts()


    app.run(
        debug=True
    )