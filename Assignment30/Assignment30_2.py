import schedule
import time
import datetime

def DisplayDateTime():
    current = datetime.datetime.now()
    print("Current time is :",current)

def DateTimeAnotherWay():
    current = datetime.datetime.now()
    print("Current another way time is :",current.strftime("%d-%m-%Y %I:%M:%S %p"))

    print("Current OnGoing Hour(24): ",current.strftime("%H"))
    print("Current OnGoing Hour(12): ",current.strftime("%I"))
    print("Current OnGoing Minute  : ",current.strftime("%M"))
    print("Current OnGoing Seconds : ",current.strftime("%S"))
    print("Current OnGoing Day     : ",current.strftime("%d"))
    print("Current OnGoing Month   : ",current.strftime("%m"))
    print("Current OnGoing Year    : ",current.strftime("%Y"))
    print("Current OnGoing Year    : ",current.strftime("%y"))
    print("Current OnGoing AM/PM   : ",current.strftime("%p"))


def main():
    schedule.every(1).seconds.do(DisplayDateTime)
    schedule.every(3).seconds.do(DateTimeAnotherWay)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()