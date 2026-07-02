Length_Greater = lambda str : len(str) > 5

def main():
    print("\nlambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.")
    a = int(input(("\nHow many strings you want to enter : ")))
    Given_list = list()

    for i in range(a):
        no = (input("Enter the String :"))
        Given_list.append(no)

    print("\nEntered list is    : ",Given_list)

    Fdata = list(filter(Length_Greater,Given_list))
    print("\nString having length greater than 5 is : ",Fdata)

if __name__ == '__main__':
    main()