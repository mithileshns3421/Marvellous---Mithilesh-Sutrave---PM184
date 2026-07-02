def main():

    find_max = lambda no1,no2 : max(no1,no2)
    print("\nlambda function which accepts two numbers and returns maximum number.")
    no1 = int(input("\nEnter first  Number :"))
    no2 = int(input("\nEnter second Number :"))

    res = find_max(no1,no2)

    print("\nMaximum of given 2 numbers is : ",res)

if __name__ == '__main__':
    main()