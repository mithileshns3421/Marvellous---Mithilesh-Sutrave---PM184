list_of_even = lambda no : no%2 == 0 

def main():
    print("\nLambda function using filter() which accepts a list of numbers and returns a list of even numbers..")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int(input("Enter the number :"))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Fdata = list(filter(list_of_even,Given_list))
    print("\nList of Even Number is : ",Fdata)

if __name__ == '__main__':
    main()