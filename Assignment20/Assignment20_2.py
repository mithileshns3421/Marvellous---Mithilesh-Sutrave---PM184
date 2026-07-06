import threading
import time

def EvenFactor(no):
    sum = 0
    for i in range(1,no+1):
        if no%i == 0 and i%2 == 0:
            sum = sum + i

    print("\nSum of EvenFactor is : ",sum)
    print(f"Exit from EvenFactor.")

def OddFactor(no):
    sum1 = 0
    for i in range(1,no+1):
        if no%i == 0 and i%2 != 0:
            sum1 = sum1 + i

    print("\nSum of OddFactor is : ",sum1)
    print(f"Exit from OddFactor.")


def main():
    print("\nPython application that creates two separate threads named EvenFactor and OddFactor.")
    a = int(input(("\nEnter the number you want to get Even/Odd Factors : ")))

    #threads Created.
    t1 = threading.Thread(target=EvenFactor,args=(a,))
    t2 = threading.Thread(target=OddFactor,args=(a,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()