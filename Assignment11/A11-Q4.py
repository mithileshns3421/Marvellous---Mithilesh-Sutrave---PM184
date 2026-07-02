def reverse_number(a):
    reverse = 0 
    while a > 0:
        digit = a % 10                           
        reverse = reverse * 10 + digit       
        a = a // 10                          

    print("Reverse of given digits is :- ",reverse)

def main():
    no1 = int(input("\nEnter the number :- "))
    reverse_number(no1)


if __name__ ==  "__main__":
    main()