def main():
    get_square = lambda no: no * no 

    a = int(input("\nEnter the number to get Square of it : "))
    result = get_square(a)
    print("\nSquare of ",a," is : ",result)

if __name__ == '__main__':
    main()
