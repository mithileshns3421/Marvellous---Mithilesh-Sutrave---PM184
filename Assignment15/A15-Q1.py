get_squares = lambda no : no * no

def main():
    print("\nLambda function using map() which accepts a list of numbers and returns a list of squares of each number.")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int(input("Enter the number :"))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Mdata = list(map(get_squares,Given_list))
    print("\nList of Squares is : ",Mdata)

if __name__ == '__main__':
    main()