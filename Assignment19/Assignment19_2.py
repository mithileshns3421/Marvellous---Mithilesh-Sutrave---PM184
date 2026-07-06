ret_mult = lambda a,b : a * b

def main():
    no1 = int(input(("\nEnter first  number :")))
    no2 = int(input(("\nEnter second number :")))
    res = ret_mult(no1,no2)
    print(f"\nMultiplication of given number {no1}, {no2} is {res}.")

if __name__ =='__main__':
    main()
