
#Uses a dictionary to track the number of each message type
log_data = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

#opens and checks the start of each line. then adds a count to the appropriate type.
def check_log():
    with open("server_logs.txt", "r") as log:
        longest_line = 0

        for line in log:
            if line.startswith("INFO"):
                log_data["INFO"] += 1
            elif line.startswith("WARNING"):
                log_data["WARNING"] += 1
            elif line.startswith("ERROR"):
                log_data["ERROR"] += 1
            else:
                pass


            if len(line) > longest_line:
                longest_line = len(line)
        #for debugging
        print(longest_line)



def main():
    check_log()
    print(f"""Log Summary
INFO: {log_data["INFO"]}
WARNING: {log_data["WARNING"]}
ERROR: {log_data["ERROR"]}
Longest message: 
""")

if __name__ == "__main__":
    main()