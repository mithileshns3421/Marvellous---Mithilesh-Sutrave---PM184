def reverse_number(a):
    reverse = 0 
    while a > 0:
        digit = a % 10                              
        reverse = reverse * 10 + digit                
        a = a // 10                             
        
    return reverse


def main():
    no1 = int(input("\nEnter the number :- "))
    rev = reverse_number(no1)
    if rev == no1:
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ ==  "__main__":
    main()