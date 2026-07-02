def main():

    find_min = lambda no1,no2 : min(no1,no2)
    print("\nlambda function which accepts two numbers and returns minimum number.")
    no1 = int(input("\nEnter first  Number :"))
    no2 = int(input("\nEnter second Number :"))

    res = find_min(no1,no2)

    print("\nMinimum of given 2 numbers is : ",res)

if __name__ == '__main__':
    main()