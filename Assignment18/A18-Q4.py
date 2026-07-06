def main():
    i = 0
    lst = list()
    print("\nWrite a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List")
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    freq_no = int(input("\nEnter the number you want to search : "))

    count = lst.count(freq_no)
    print(f"\nEntered number is {count} times in the list using count method.")

    cnt = 0
    for i in lst:
        if freq_no == i:
            cnt = cnt + 1

    print(f"\nEntered number is {freq_no} is {cnt} times in the given list using loop method.")

if __name__ == '__main__':
    main()