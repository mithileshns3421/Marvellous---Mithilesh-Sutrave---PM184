import sys
import os
import psutil
import datetime

def CreateLogFile():
    filename = "Assignment34_1_ProcessLog.log"
    if not os.path.exists(filename):
        with open(filename, "w"):
            pass
    return filename


def WriteLog(message):
    logfile = CreateLogFile()
    with open(logfile, "a") as file:
        time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        file.write(f"[{time}] {message}\n")

def Help():

    print("""
-------------------------------------------------------
Usage :

python Assignment34_1.py

This application displays all running processes with their PID, Process Name and Username.

Output is stored in Assignment34_1_ProcessLog.log
-------------------------------------------------------
""")


def DisplayProcessInformation():
    WriteLog("Process Monitoring Started")
    WriteLog("-" * 70)
    WriteLog("{:<10}{:<35}{}".format("PID", "Process Name", "Username"))
    WriteLog("-" * 70)

    count = 0
    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            WriteLog("{:<10}{:<35}{}".format(pid,
                                             str(name),
                                             str(username)))

            count += 1
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            continue

    WriteLog("-" * 70)
    WriteLog(f"Total Running Processes : {count}")
    WriteLog("Process Monitoring Completed")


def main():
    if len(sys.argv) > 2:
        print("Invalid Number of Arguments")
        return

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "-h":
            Help()
            return
        elif sys.argv[1].lower() == "-u":
            Help()
            return

    try:
        DisplayProcessInformation()
        print("Process information stored in Assignment34_1_ProcessLog.log")

    except Exception as e:
        WriteLog(str(e))

if __name__ == "__main__":
    main()
    