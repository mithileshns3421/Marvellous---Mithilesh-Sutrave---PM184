from functools import reduce

get_sum_of_all = lambda no1,no2 : no1 + no2

def main():
    print("\nlambda function using reduce() which accepts a list of numbers and returns the addition of all elements")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int(input("Enter the number :"))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Rdata = reduce(get_sum_of_all,Given_list)
    print("\nAddition of All Elements is : ",Rdata)

if __name__ == '__main__':
    main()