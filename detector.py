from collections import defaultdict
from database import insert_alert


def detect_threats(logs):

    failed_attempts = defaultdict(int)

    for log in logs:

        event_type = log["event_type"]
        source = log["source"]

        if event_type == "LOGIN_FAILED":
            failed_attempts[source] += 1

    for ip, count in failed_attempts.items():

        if count >= 3:

            insert_alert(
                "CRITICAL",
                f"Possible Brute Force Attack from {ip}"
            )

        elif count >= 1:

            insert_alert(
                "MEDIUM",
                f"Failed Login Attempt from {ip}"
            )