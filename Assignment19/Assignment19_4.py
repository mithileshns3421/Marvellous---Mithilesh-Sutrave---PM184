from functools import reduce

FIND_EVEN = lambda no1 : no1%2 == 0 

EVEN_NO_SQUARE = lambda no2 : no2 * no2

ADD_SQUARE = lambda a,b : a + b

def main():
    i = 0
    lst = list()
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    Fdata = list(filter(FIND_EVEN,lst))
    print("\nFiltered List which are Even number ",Fdata)

    Mdata = list(map(EVEN_NO_SQUARE,Fdata))
    print("\nSquare of above even numbers ",Mdata)

    Rdata = reduce(ADD_SQUARE,Mdata)
    print("\nAddition of all Squares ",Rdata)


if __name__ =='__main__':
    main()