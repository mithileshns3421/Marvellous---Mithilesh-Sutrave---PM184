from functools import reduce

AddnofAll = lambda no1,no2 : no1 + no2


def main():
    i = 0
    lst = list()
    print("\nProgram which accept N numbers from user and store it into List. Return addition of all elements from that List")
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    Rdata = reduce(AddnofAll,lst)
    print("\nAddition of all elements is :",Rdata)

if __name__ == '__main__':
    main()