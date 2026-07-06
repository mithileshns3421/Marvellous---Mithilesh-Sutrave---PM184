def display_star(no):
    for i in range (no):
        print("     *" * 5 )

def main():
    print("\n************* Write a program which accept one number and display below pattern *************")
    a = int(input("\nEnter the number :- "))
    display_star(a)

if __name__ ==  "__main__":
    main()