
Div_by_3_5 = lambda no : (no%3 == 0 and no%5 == 0)

def main():
    print("\nlambda function using filter() which accepts a list of numbers and returns a list of numbers ")
    print("divisible by both 3 and 5..")
    a = int(input(("\nHow many numbers you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = int((input("Enter the number :")))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Fdata = list(filter(Div_by_3_5,Given_list))
    print("\nGiven is ths list which is Divisible by both 3&5 : ",Fdata)

if __name__ == '__main__':
    main()