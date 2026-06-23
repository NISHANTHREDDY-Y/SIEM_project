import sqlite3

DB_PATH = "data/siem.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        event_type TEXT,
        username TEXT,
        source TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        severity TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(timestamp, event_type, username, source):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO logs
    (timestamp, event_type, username, source)
    VALUES (?, ?, ?, ?)
    """, (
        timestamp,
        event_type,
        username,
        source
    ))

    conn.commit()
    conn.close()


def insert_alert(severity, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alerts
    (severity, message)
    VALUES (?, ?)
    """, (
        severity,
        message
    ))

    conn.commit()
    conn.close()


def get_logs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM logs
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_alerts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM alerts
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def clear_logs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logs")

    conn.commit()
    conn.close()


def clear_alerts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alerts")

    conn.commit()
    conn.close()