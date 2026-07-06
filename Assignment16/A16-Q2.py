def CheckNum(a):
    if a%2==0:
        print("\nEntered number",a,"is Even.")
    else:
        print("\nEntered number",a,"is Odd.")

def main():
    print("\nFunction to check EVEN / ODD for given number")
    a = int(input("\nEnter number to check Even or Odd :"))
    CheckNum(a)

if  __name__ == "__main__":
    main()