def Add(a,b):
    c = a + b
    return c

def main():
    print("\nFunction to Add given two numbers.")
    no1 = int(input("\nEnter first  number  :"))
    no2 = int(input("\nEnter second number  :"))
    res = Add(no1,no2)

    print("\nAddition of given numbers is : ",res)

if  __name__ == "__main__":
    main()