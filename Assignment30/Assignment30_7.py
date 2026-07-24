import os
import shutil
import schedule
import time
import datetime


def backup_file(source_file, destination_folder):
    try:      

        ret = False
        ret = os.path.exists(destination_folder)
        dir_name = os.path.basename(destination_folder)

        if ret == False:
            print(f"\nMarvellous Automation Error : NO SUCH DIRECTORY IS AVAILABLE WITH NAME {dir_name} .")
            print(f"Dont worry we have created a folder with name {dir_name} .")
            os.makedirs(destination_folder, exist_ok=True)         

        # Get file name and extension
        file_name = os.path.basename(source_file)
        name, ext = os.path.splitext(file_name)

        # Current date and time
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Backup file name
        backup_name = f"{name}_{timestamp}{ext}"

        # Destination path
        destination_path = os.path.join(destination_folder, backup_name)

        # Copy file
        shutil.copy2(source_file, destination_path)

        # Write log
        with open("backup_log.txt", "a") as log:
            log.write(f"Backup completed Successfully at : {datetime.datetime.now()} \n")

        print("\nBackup Created Successfully")
        print("\nBackup File :", destination_path)

    except Exception as e:
        print("Error:", e)


def main():
    source = input("\nEnter Source File Path with File Name : ")
    destination = input("\nEnter Destination Folder Path    : ")

    if not os.path.isfile(source):
        print("\nSource file does not exist.")
        return           

    # First backup immediately
    backup_file(source, destination)


    # Scheduling backup for every hour
    schedule.every(30).minutes.do(backup_file, source, destination)

    print("\nBackup Scheduler Started Now ------> ",time.ctime())
    print("Backup will run for every 30 minutes now.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
