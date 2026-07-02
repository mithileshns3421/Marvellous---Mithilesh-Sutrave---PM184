from functools import reduce

min_of_all = lambda no1,no2 : no1 if no1 < no2 else no2

def main():
    print("\nlambda function using reduce() which accepts a list of numbers and returns the minimum elements")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int(input("Enter the number :"))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Rdata = reduce(min_of_all,Given_list)
    print("\Minimum from given Elements is : ",Rdata)

if __name__ == '__main__':
    main()