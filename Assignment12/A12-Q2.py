def print_factors(no1):
    for i in range(1,no1+1):
        if no1%i == 0:
            print("Factors are :-",i)


def main():
    a = int(input("\nEnter the Number to print Factors :- "))
    print_factors(a)

if __name__ == "__main__":
    main()