import os
import datetime
import psutil
import sys
import os

def CreateLog(directory):

    filename = "Assignment_34_3_ProcessLog.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write("=" * 70 + "\n")
        file.write("Running Process Information\n")
        file.write("=" * 70 + "\n")

    return filepath


def WriteLog(filepath, message):
    with open(filepath, "a") as file:
        file.write(message + "\n")

def ProcessInformation(logfile):
    count = 0
    header = "{:<10}{:<35}{}".format("PID",
                                     "Process Name",
                                     "Username")

    WriteLog(logfile, header)
    WriteLog(logfile, "-" * 70)

    for process in psutil.process_iter(['pid',
                                        'name',
                                        'username']):

        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            data = "{:<10}{:<35}{}".format(pid,
                                           str(name),
                                           str(username))

            WriteLog(logfile, data)
            count += 1

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):

            continue

    WriteLog(logfile, "-" * 70)
    WriteLog(logfile, "Total Running Processes : {}".format(count))


def Help():

    print("""
----------------------------------------------------
Usage :
python Assignment34_3.py DirectoryName
----------------------------------------------------
""")


def main():

    if len(sys.argv) != 2:
        Help()
        return

    if sys.argv[1] in ("-h", "--help"):
        Help()
        return

    directory = sys.argv[1]

    if not os.path.exists(directory):
        print("Directory does not exist")
        os.mkdir(directory)
        print(f"\nNew Directory {directory} created.")
    else:
        print(f"\nDirectory {directory} already exists.")

    try:
        logfile = CreateLog(directory)
        ProcessInformation(logfile)
        print("Log File Created Successfully")
        print("Log file path is : ",logfile)

        
    except Exception as eobj:
        print("Error :",eobj)


if __name__ == "__main__":
    main()