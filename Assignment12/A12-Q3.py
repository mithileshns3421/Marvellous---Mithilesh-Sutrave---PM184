def return_all_4_calc(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    mul = no1 * no2
    div = no1 / no2

    return add, sub, mul, div


def main():
    print("\n********** Calculation **********")
    a = int(input("\nEnter first  Number :- "))
    b = int(input("Enter second Number :- "))
    a,s,m,d = return_all_4_calc(a,b)

    
    print("\nAddition        is : ",a)
    print("Substraction    is : ",s)
    print("Multiplication  is : ",m)
    print("Division        is : ",d)

if __name__ == "__main__":
    main()