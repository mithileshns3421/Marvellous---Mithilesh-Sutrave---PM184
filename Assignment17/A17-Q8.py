def display_pattern(no):
    for i in range (1,no+1):
        for j in range (i):
            print(j+1,end='       ')
        print()


def main():
    print("\n************* Write a program which accept one number and display below pattern *************")
    a = int(input("\nEnter the number :- "))
    display_pattern(a)
 


if __name__ ==  "__main__":
    main()