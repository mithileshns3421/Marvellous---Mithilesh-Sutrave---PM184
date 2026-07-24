import schedule
import time
import datetime
import sys

def Display():
  
    fname = open("Marvellous.txt","a")

    current = datetime.datetime.now()

    with fname as fobj:
        fobj.write("Task Executed at : " + str(current.strftime("%H")) +':'+ str(current.strftime("%M")) +':' + str(current.strftime("%S"))+' '+ str(current.strftime("%p")) + "\n")

    fobj.close()
    
def main():
        schedule.every(2).seconds.do(Display)

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()