import multiprocessing
import time
import os


def SumSquare(a):
    print("Process is running with PID : ",os.getpid())
    sum = 0
    for i in range(1,a+1):
        sum += (i ** 2)

    return sum

def main():
    emp_list  = list()

    no = int(input("\nEnter how many number you want to enter in list : "))
    for i in range(1,no+1):
        a = int(input("\nEnter the value to put into list : "))
        emp_list.append(a)

    print("\nEntered list is : ",emp_list)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    
    result = pobj.map(SumSquare,emp_list)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("\nList for Sum of Square is : ",result)
    print(f"\nTime Required is : {end_time - start_time:.4f} Seconds")


if __name__ == "__main__":
    main()