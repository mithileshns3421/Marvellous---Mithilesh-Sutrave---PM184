from functools import reduce

product_of_all = lambda no1,no2 : no1 * no2

def main():
    print("\nlambda function using reduce() which accepts a list of numbers and returns the product of all elements. ")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int((input("Enter the number :")))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Rdata = reduce(product_of_all,Given_list)
    print("\nProduct of all elements is : ",Rdata)

if __name__ == '__main__':
    main()