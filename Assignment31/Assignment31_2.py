import schedule
import time


def Display(a):
    print(f"\nMessage give is : {a} at {time.ctime()}")

def main():

    message = input("Enter the message you want to display : ")

    schedule.every(3).seconds.do(Display,message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
