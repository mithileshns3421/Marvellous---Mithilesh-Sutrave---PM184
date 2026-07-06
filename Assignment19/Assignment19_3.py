from functools import reduce

GT70_LT90 = lambda no1 : (no1 >= 70 and no1 <= 90) 

INCR_BY_10 = lambda no2 : no2 + 10

TOTAL_PRODUCT = lambda a,b : a * b

def main():
    i = 0
    lst = list()
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    Fdata = list(filter(GT70_LT90,lst))
    print("\nFiltered List which is greater than 70 and less than 90 is ",Fdata)

    Mdata = list(map(INCR_BY_10,Fdata))
    print("\nNumber increased by 10 in each list is ",Mdata)

    Rdata = reduce(TOTAL_PRODUCT,Mdata)
    print("\nProduct of the numbers is ",Rdata)


if __name__ =='__main__':
    main()