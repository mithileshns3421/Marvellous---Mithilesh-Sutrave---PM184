import schedule
import time
import datetime

def Display():
    current = datetime.datetime.now()

    print("Current OnGoing Hour(24): ",current.strftime("%H"))
    print("Current OnGoing Minute  : ",current.strftime("%M"))

    print("\nNamaskar..")


def main():
    schedule.every().day.at("11:20").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
