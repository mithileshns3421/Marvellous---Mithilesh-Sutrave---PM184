factorial = lambda a : 1 if a ==1 else a * factorial(a-1)

#def factorial(a):
#    if a == 1 : 
#        return 1
#    else:
#        return a * factorial(a-1)
    
def main():

    print("\n************* Program which accept number from user and return its factorial. *************")
    no = int(input("\nEnter the number : "))
    res = factorial(no)
    print("\nFactorial of givne number is : ",res)

if  __name__ == "__main__":
    main()