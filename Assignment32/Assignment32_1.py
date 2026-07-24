import time
import schedule
import datetime

def CreateFile():
    filename = datetime.datetime.now().strftime("File_%d%m%Y_%H%M%S.txt")

    fobj = open(filename,'w')
    fobj.write(f"\nFilename is   : {filename}")
    fobj.write(f"\nCreation Date : {datetime.datetime.now().strftime("%d-%m-%Y")}")
    fobj.write(f"\nCreation Time : {datetime.datetime.now().strftime("%H:%M:%S")}")

    fobj.close()

def main():
    schedule.every(5).seconds.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)
    


if __name__ == "__main__":
    main()
