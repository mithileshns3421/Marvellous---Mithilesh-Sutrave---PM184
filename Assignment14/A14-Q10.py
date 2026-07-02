def main():
    #largest_of_3 = lambda no1,no2,no3 : max(no1,no2,no3)
    print("\nlambda function which accepts three numbers and returns largest number\n")
    largest_of_3 = lambda no1,no2,no3 : no1 if (no1 >= no2 and no1 >= no3) else (no2 if no2 >= no3 else no3)

    no1 = int(input("Enter first  Number :"))
    no2 = int(input("Enter second Number :"))
    no3 = int(input("Enter third  Number :"))

    res = largest_of_3(no1,no2,no3)
 
    print("\nAddition of given two numbers is : ",res)

if __name__ == '__main__':
    main()