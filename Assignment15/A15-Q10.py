get_even_number = lambda no : no%2 == 0 

def main():
    print("\nlambda function using filter() which accepts a list of numbers and returns the count of even numbers. ")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int((input("Enter the number :")))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Fdata = len(list(filter(get_even_number,Given_list)))
    print("\nList of All Even Number is : ",Fdata)

if __name__ == '__main__':
    main()