def number_check(a):
    if a%5 == 0:
        return True
    else:
        return False
def main():
    print("\nProgram to check whether that number is divisible by 5, TRUE/FALSE")
    no = int(input("\nEnter the number you want to check : "))
    ret = number_check(no)
    if ret:
        print("True")
    else:
        print("False")
    
if  __name__ == "__main__":
    main()