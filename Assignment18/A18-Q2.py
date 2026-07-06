from functools import reduce

MaxiofAll = lambda no1,no2 : no1 if no1 > no2 else no2 


def main():
    i = 0
    lst = list()
    print("\nProgram which accept N numbers from user and store it into List. Return Maximum of all elements from that List")
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    Rdata = reduce(MaxiofAll,lst)
    print("\nMaximum from all given elements is :",Rdata)

if __name__ == '__main__':
    main()