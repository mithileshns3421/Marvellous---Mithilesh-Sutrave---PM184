from functools import reduce 
from MarvellousNum import ChkPrime

def ListPrime(Data):
    Fdata = list(filter(ChkPrime,Data))
    print("\nOnly Prime numbers from the list are  : ",Fdata)

    return reduce (lambda no1,no2 : no1+no2, Fdata )

def main():
    i = 0
    lst = list()
    print("\nWrite a program which accept N numbers from user and store it into List. Returns addition of all prime numbers")
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)
    print("\nSummation of all prime numbers is : ",ListPrime(lst))


if __name__ == '__main__':
    main()