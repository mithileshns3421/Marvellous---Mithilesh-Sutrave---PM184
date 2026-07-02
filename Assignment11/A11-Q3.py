def sum_of_digits(a):
    sum_digit = 0 
    while a > 0:
        digit = a % 10                     
        sum_digit += digit                 
        a = a // 10                     

    print("Sum of given digits is :- ",sum_digit)

def main():
    no1 = int(input("\nEnter the number :- "))
    sum_of_digits(no1)

if __name__ ==  "__main__":
    main()