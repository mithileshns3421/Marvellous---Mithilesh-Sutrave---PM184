import schedule
import time
import datetime

def CreateLogFile():
    filename = datetime.datetime.now().strftime("MarvellousLog_%d%m%Y_%H%M%S.txt")

    fobj = open(filename,'w')
    fobj.write(f"Log File Created Successfully, Creation time : {time.ctime()} ")

#    with open(filename,"w") as fobj:
#        fobj.write(f"Log File Created Successfully, Creation time : {time.ctime()} ")   

    print("\nLog File created successfully.")

    fobj.close()

def main():
    schedule.every(1).minutes.do(CreateLogFile)
    
    print("\nScheduler Started...")
    print("A new log file will be created every 1 minute.\n")    
    
    
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()