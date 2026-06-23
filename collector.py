import win32evtlog
from database import insert_log


def collect_windows_logs():

    server = "localhost"

    logs_to_read = [
        "Security",
        "System",
        "Application"
    ]


    total = 0


    try:

        for log_type in logs_to_read:


            hand = win32evtlog.OpenEventLog(
                server,
                log_type
            )


            flags = (
                win32evtlog.EVENTLOG_BACKWARDS_READ |
                win32evtlog.EVENTLOG_SEQUENTIAL_READ
            )


            events = win32evtlog.ReadEventLog(
                hand,
                flags,
                0
            )


            for event in events:


                event_id = event.EventID & 0xFFFF


                timestamp = event.TimeGenerated.Format()


                username = extract_username(event)


                source = server


                event_type = get_event_type(event_id)



                insert_log(
                    timestamp,
                    event_type,
                    username,
                    source
                )


                total += 1



                if total >= 100:
                    break



            if total >= 100:
                break



        print(
            f"{total} Windows events collected"
        )



    except Exception as e:

        print(
            "Windows collector error:",
            e
        )





def extract_username(event):


    username = "SYSTEM"


    if event.StringInserts:


        for item in event.StringInserts:


            if item:


                value = str(item)



                # Common username patterns

                if (
                    "\\" in value
                    or
                    value.lower() == "administrator"
                    or
                    value.lower() == "admin"
                ):

                    username = value

                    break



    return username





def get_event_type(event_id):


    event_map = {


        4624:
        "SUCCESSFUL_LOGIN",


        4625:
        "FAILED_LOGIN",


        4634:
        "USER_LOGOFF",


        4647:
        "LOGOFF",


        4672:
        "ADMIN_PRIVILEGE_USED",


        4720:
        "USER_CREATED",


        4726:
        "USER_DELETED",


        4732:
        "USER_ADDED_TO_GROUP"


    }



    return event_map.get(
        event_id,
        f"WINDOWS_EVENT_{event_id}"
    )