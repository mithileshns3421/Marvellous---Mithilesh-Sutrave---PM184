def main():
    multiplication = lambda no1,no2 : no1 * no2

    print("\nlambda function which accepts two numbers and returns multiplication.")
    no1 = int(input("Enter first  Number :"))
    no2 = int(input("Enter second Number :"))
    res = multiplication(no1,no2)
 
    print("\nAddition of given two numbers is : ",res)

if __name__ == '__main__':
    main()