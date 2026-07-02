def CheckGreater(a,b):
    if a > b:
        print("\n",a,"is the greater than",b)
    else:
        print("\n",b,"is the greater than",a)


def main():
    No1 = int(input("Enter first  Number :- "))
    No2 = int(input("Enter second Number :- "))
    CheckGreater(No1,No2)

if __name__ == "__main__":
    main()