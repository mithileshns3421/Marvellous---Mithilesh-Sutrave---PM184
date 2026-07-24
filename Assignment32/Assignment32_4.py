import os
import shutil
import schedule
import time
import datetime


def copy_text_files(source_dir, destination_dir):

    # Log file
    log_file = datetime.datetime.now().strftime("LogFile_%d%m%Y_%H%M%S.txt")

    # Get all files from source directory
    for file in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file)

        # Copy only .txt files
        if os.path.isfile(source_path) and file.endswith(".txt"):
            destination_path = os.path.join(destination_dir, file)
            try:
                shutil.copy2(source_path, destination_path)
                print(file, "Copied Successfully")
                with open(log_file, "a") as log:
                    log.write(f"{datetime.datetime.now()} : {file} Copied Successfully\n")

            except Exception as eobj:
                print(file, "Could not be copied.")
                with open(log_file, "a") as log:
                    log.write(f"{datetime.datetime.now()} : {file} Failed - {eobj}\n")


def main():

    source      = input("\nEnter Source Directory     : ")
    destination = input("Enter Destination Directory  : ")

    # Validate directories
    if not os.path.isdir(source):
        print("Invalid Source Directory")
        return

    if not os.path.isdir(destination):
        print("Invalid Destination Directory")
        return

    # First execution
    copy_text_files(source, destination)

    # Schedule every 10 minutes
    schedule.every(5).seconds.do(copy_text_files, source, destination)

    print("\nScheduler Started...")
    print("Copying .txt files every 10 minutes...\n")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()