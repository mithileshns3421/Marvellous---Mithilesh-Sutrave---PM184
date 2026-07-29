import sys
import os
import datetime
import psutil

def CreateLogFile():
    filename = "Assignment34_2_ProcessLog.log"
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

python Assignment34_2.py notepad.exe

This application displays given running processes
with their PID, Process Name and Username if it is running.

Output is stored in Assignment34_2_ProcessLog.log
-------------------------------------------------------
""")

def DisplayProcessInfo(ProcessName):
    Found = False
    WriteLog("=" * 70)
    WriteLog(f"Searching Process : {ProcessName}")
    WriteLog("=" * 70)

    try:

        for process in psutil.process_iter(['pid',
                                            'name',
                                            'username',
                                            'status',
                                            'memory_info']):

            try:
                name = process.info['name']
                if name is not None and name.lower() == ProcessName.lower():

                    Found = True

                    WriteLog(f"Process Name : {name}")
                    WriteLog(f"PID          : {process.info['pid']}")
                    WriteLog(f"Username     : {process.info['username']}")
                    WriteLog(f"Status       : {process.info['status']}")

                    memory = process.info['memory_info'].rss / (1024 * 1024)

                    WriteLog(f"Memory Usage : {memory:.2f} MB")

                    WriteLog("-" * 70)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                continue

        if not Found:
            WriteLog("Process is not running.")

    except Exception as e:
        WriteLog("Error : " + str(e))


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

        process_name = sys.argv[1]
        DisplayProcessInfo(process_name)

        print("Process information stored in Assignment34_2_ProcessLog.log")

    except Exception as e:

        WriteLog(str(e))


if __name__ == "__main__":
    main()