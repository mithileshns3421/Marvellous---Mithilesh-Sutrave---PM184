import threading
import time

def SumEven(no):
    for i in range(2,no+1,2):
        if i%2 == 0:
            print(f" {i} is Even Number")        

    print("Exit from SumEven Thread..")

def SumOdd(no):
    for i in range(1,no+1,2):
        if i%2 != 0:
            print(f" {i} is Odd Number")

    print("Exit from SumOdd Thread..")


def main():
    print("\nPython application that creates two separate threads named Even and Odd.")
    a = int(input(("\nEnter till how many you want to get Even/Odd numbers : ")))

    #threads Created.
    t1 = threading.Thread(target=SumEven,args=(a,))
    t2 = threading.Thread(target=SumOdd,args=(a,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()