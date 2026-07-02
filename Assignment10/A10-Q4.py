def print_even_number(a):
    even_list = []
    for i in range(1,a+1):
        if i%2 == 0:
            even_list.append(i)

    print("List of all Even Numbers is :- ",even_list)

def main():
    a = int(input("Enter the number :- "))
    print_even_number(a)

if __name__ ==  "__main__":
    main()