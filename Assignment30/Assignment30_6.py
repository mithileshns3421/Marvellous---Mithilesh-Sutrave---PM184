import schedule
import time
import datetime

def Lunch():
    current = datetime.datetime.now()

    print("Current time is : " + current.strftime("%H") + ':' + current.strftime("%M") + ' ' + current.strftime("%p"))
 
    print("Lunch Time....")

def Wrapup():
    current = datetime.datetime.now()

    print("Current time is : " + current.strftime("%H") + ':' + current.strftime("%M") + ' ' + current.strftime("%p"))

    print("Wrap up Work...")


def main():
    schedule.every().day.at("12:19").do(Lunch)
    schedule.every().day.at("12:24").do(Wrapup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
