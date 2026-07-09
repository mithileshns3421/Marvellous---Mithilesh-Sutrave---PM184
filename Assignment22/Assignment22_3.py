import multiprocessing
import time
import os


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Function to count prime numbers from 1 to N
def count_primes(n):
    count = 0

    for i in range(2, n + 1):
        if is_prime(i):
            count += 1

    return count

def main():
    emp_list  = list()

    no = int(input("\nEnter how many number you want to enter in list : "))
    for i in range(1,no+1):
        a = int(input("Enter the value to put into list : "))
        emp_list.append(a)


    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()    
    result = pobj.map(count_primes,emp_list)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print("\nEntered list is : ",emp_list)

    print("\nList for Prime numbers in all given number is : ",result)
    print(f"\nTime Required is : {end_time - start_time:.4f} Seconds")


if __name__ == "__main__":
    main()