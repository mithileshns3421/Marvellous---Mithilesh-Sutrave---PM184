def add_of_digit(a):
    cnt = 0 
    while a > 0:
        no = a%10
        cnt = cnt + no
        a = a // 10 
        
    print("Sum of total number of Digits in given number is : ",cnt)


def main():
    print("\nprogram which accept number from user and return addition of digits in that number")
    no = int(input("Enter the number : "))
    add_of_digit(no)

if  __name__ == "__main__":
    main()