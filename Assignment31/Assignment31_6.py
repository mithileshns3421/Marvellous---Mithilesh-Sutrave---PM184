import schedule
import time

def start():
    print("\nStart your weekly Goals.")

def review():
    print("\nReview your weekly Goals.")

def complete():
    print("\nComplete your weekly Goals.")



def main():

    print("\nCurrent date and time : ",time.ctime())

    schedule.every().monday.at("09:00").do(start)
    schedule.every().wednesday.at("21:48").do(review)
    schedule.every().friday.at("18:00").do(complete)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()