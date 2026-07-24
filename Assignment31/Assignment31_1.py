import schedule
import time


def Display(a):
    print(f"{a} ---> Time is :{time.ctime()}")

def main():

    input_second  = int(input("Enter in how many seconds you want to print the message : "))
    input_message = input("Enter the message you want to display : ")

    schedule.every(input_second).seconds.do(Display,input_message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
