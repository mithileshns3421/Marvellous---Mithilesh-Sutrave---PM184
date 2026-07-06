import threading
import time
import sys

def num1to50(Data):
    print("Thread1 Started...... ")
    for i in range(1,Data+1):
        print(i)

    print("Thread1 Completed...... ")

def num50to1(Data):
    print("\nThread2 Started...... ")
    for i in range(Data,0,-1):
        print(i)

    print("Thread2 Completed...... ")

def main():

    no = int(input("\nEnter the number for straight and reverse display of number : "))
    #no = int(sys.argv[1]) #tried using Command line Argument.

    #threads Created.
    t1 = threading.Thread(target=num1to50,args=(no,))
    t2 = threading.Thread(target=num50to1,args=(no,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()