def number_check(a):
    if a == 0:
        print("Zero")
    elif a > 0:
        print("Postive")
    else:
        print("Negative")

def main():
    print("\nProgram to check whether that number is positive or negative or zero")
    no = int(input("\nEnter the number you want to check : "))
    number_check(no)
    
if  __name__ == "__main__":
    main()