def main():
    get_cube = lambda no: no * no * no

    print("\nlambda function which accepts one number and returns Cube of that number")
    a = int(input("\nEnter the number to get Cube of it : "))
    result = get_cube(a)
    print("\nCube of ",a," is : ",result)

if __name__ == '__main__':
    main()
