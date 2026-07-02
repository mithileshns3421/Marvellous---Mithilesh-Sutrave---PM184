check = lambda no : True if no%2 == 0 else False

def main():
    print("\nProgram will returns True if number is EVEN otherwise False.")
    no = int(input("\nEnter the number : "))
    res = check(no)

    print("Output :",res)

if __name__ == '__main__':
    main()
