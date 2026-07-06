chk_prime = lambda a : a ** 2

def main():
    no = int(input(("\nEnter the number :")))
    res = chk_prime(no)
    print(f"\nPower of 2 for given number {no} is {res} ")

if __name__ =='__main__':
    main()
