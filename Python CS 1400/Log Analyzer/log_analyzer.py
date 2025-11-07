
#opens and checks the start of each line. then adds a count to the appropriate type.
def check_log(log_data):
    with open("server_logs.txt", "r") as log:
        longest_line = 0
        longest_message = ""

        for line in log:
            error_messages = line.split("|")

            if error_messages[0] == "INFO":
                log_data["INFO"] += 1
            elif error_messages[0] == "WARNING":
                log_data["WARNING"] += 1
            elif error_messages[0] == "ERROR":
                log_data["ERROR"] += 1
            else:
                pass

            # Compares the length of the messages only(not the code) then
            if len(error_messages[1]) > longest_line:
                longest_line = len(error_messages[1])
                longest_message = error_messages[1]
        return longest_message


def main():
    # Uses a dictionary to track the number of each message type
    log_data = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }


    longest_message = check_log(log_data)

    print(f"""Log Summary
INFO: {log_data["INFO"]}
WARNING: {log_data["WARNING"]}
ERROR: {log_data["ERROR"]}
Longest message: {longest_message}
""")

if __name__ == "__main__":
    main()