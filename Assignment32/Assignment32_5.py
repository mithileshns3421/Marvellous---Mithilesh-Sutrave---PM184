import os
import schedule
import time
import datetime


def delete_empty_files(directory):

    log_file = datetime.datetime.now().strftime("LogFile_%d%m%Y_%H%M%S.txt")

    for folder, subfolders, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(folder, file)
            try:
                # Check whether file is empty
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    print("Deleted :", file_path)
                    with open(log_file, "a") as log:
                        log.write(f"{datetime.datetime.now()} : Deleted -> {file_path}\n")

            except PermissionError:
                print("Permission Denied :", file_path)
                with open(log_file, "a") as log:
                    log.write(f"{datetime.datetime.now()} : Permission Denied -> {file_path}\n")
            except FileNotFoundError:
                print("File Not Found :", file_path)
            except Exception as e:
                print("Error :", e)

def main():

    directory = input("\nEnter the directory path : ")
    print()

    # Validate directory
    if not os.path.isdir(directory):
        print("Invalid Directory")
        return

    # Run immediately
    delete_empty_files(directory)

    # Schedule every hour
    schedule.every(1).hours.do(delete_empty_files, directory)

    print("\nScheduler Started...")
    print("Empty files will be deleted every hour.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()