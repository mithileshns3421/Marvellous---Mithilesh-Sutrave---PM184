def add_of_factors(a):
    sum = 0


    for i in range(1,a+1):
        if a%i == 0:
            sum = sum + i
            print("Factors are:",i,end=" ")
    return sum


def main():

    print("\n************* Program which accept one number from user and return addition of its factors. *************")
    no = int(input("\nEnter the number : "))
    res = add_of_factors(no)
    print("\nAddition of Factors of Given number is : ",res)

if  __name__ == "__main__":
    main()