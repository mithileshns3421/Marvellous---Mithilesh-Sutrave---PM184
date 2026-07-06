def display_pattern(no):
    for i in range (no,0,-1):
        for j in range (i):
            print(i,end='       ')
        print()
        
def main():
    print("\n************* Write a program which accept one number and display below pattern *************")
    a = int(input("\nEnter the number :- "))
    display_pattern(a)
 


if __name__ ==  "__main__":
    main()