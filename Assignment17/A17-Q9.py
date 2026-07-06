def no_of_digit(a):
    b = str(a)    
    print("Total number of Digits in given number is : ",(len(b)))

def main():
    print("\nprogram which accept number from user and return number of digits in that number")
    no = int(input("Enter the number : "))
    no_of_digit(no)

if  __name__ == "__main__":
    main()