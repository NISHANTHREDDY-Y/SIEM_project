def parse_log(log_line):

    parts = log_line.strip().split()

    if len(parts) < 5:
        return None

    timestamp = parts[0] + " " + parts[1]
    event_type = parts[2]

    username = "Unknown"
    source = "Unknown"

    for item in parts[3:]:

        if item.startswith("user="):
            username = item.split("=", 1)[1]

        elif item.startswith("ip="):
            source = item.split("=", 1)[1]

        elif item.startswith("target="):
            source = item.split("=", 1)[1]

    return {
        "timestamp": timestamp,
        "event_type": event_type,
        "username": username,
        "source": source
    }