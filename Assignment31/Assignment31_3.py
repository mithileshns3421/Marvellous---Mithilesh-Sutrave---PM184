import os
import time
from datetime import datetime


def scan_directory(path):
    file_count = 0
    dir_count = 0

    # Scan all items in the directory
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            file_count += 1
        elif os.path.isdir(full_path):
            dir_count += 1

    print("*" * 40)
    print("Directory Scanned    :", path)
    print("Total Files          :", file_count)
    print("Total Subdirectories :", dir_count)
    print("Scan Time            :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 40)


def main():
    directory_path = input("Enter directory path: ")

    if not os.path.exists(directory_path):
        print("\nInvalid directory path.")
        return

    while True:
        scan_directory(directory_path)
        time.sleep(60)


if __name__ == "__main__":
    main()