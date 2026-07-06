import Arithmetic

def main():
    print("\n************* Write a program which accept one number and display below pattern *************")
    a = int(input("\nEnter the number :- "))
    b = int(input("\nEnter the number :- "))

    addn = Arithmetic.addition(a,b)
    print("\nAddition is : ",addn)
    subs = Arithmetic.substraction(a,b)
    print("\nSubstractin is : ",subs)
    mult = Arithmetic.multiplication(a,b)
    print("\nMultiplication is : ",mult)
    divs = Arithmetic.division(a,b)
    print("\nDivision is : ",divs)



if __name__ ==  "__main__":
    main()