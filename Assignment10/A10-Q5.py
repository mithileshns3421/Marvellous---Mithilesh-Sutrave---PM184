def print_odd_number(a):
    even_list = []
    for i in range(1,a+1):
        if i%2 != 0:
            even_list.append(i)

    print("List of all Odd Numbers is :- ",even_list)

def main():
    a = int(input("Enter the number :- "))
    print_odd_number(a)

if __name__ ==  "__main__":
    main()