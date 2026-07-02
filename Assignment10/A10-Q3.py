def factorial(a):
    cnt = 1
    for i in range(1,a+1):
        cnt = cnt * i

    return cnt    

def main():
    a = int(input("Enter the number :- "))
    cnt = factorial(a)
    print("Factorial of given Number is :- ",cnt)    

if __name__ ==  "__main__":
    main()