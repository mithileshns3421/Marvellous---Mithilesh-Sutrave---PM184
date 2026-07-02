def check_if_prime_number(a):
    if a == 1:
        print("\nGiven number is not a prime number")    
    elif a%2 != 0:
        print("\nGiven number is prime number")
    else:
        print("\nGiven number is not a prime number")

def main():
    a = int(input("\nEnter the number :- "))
    check_if_prime_number(a)

if __name__ ==  "__main__":
    main()