def display_num(no):
    for i in range (1,no+1):
        print(i,end='       ')
    print()    
        
def main():
    print("\n************* Write a program which accept one number and display below pattern *************")
    a = int(input("\nEnter the number :- "))
    display_num(a)
    display_num(a)
    display_num(a)
    display_num(a)
    display_num(a)


if __name__ ==  "__main__":
    main()