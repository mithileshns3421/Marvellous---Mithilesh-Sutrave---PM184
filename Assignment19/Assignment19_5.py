from functools import reduce

MULT_PRIME_BY_2 = lambda no2 : no2 * 2
MAX_OF_MAP_LIST = lambda a,b : max(a,b)


def main():
    i = 0
    lst = list()
    a = int(input("\nEnter how many number you want to enter : "))
    while i < a:
        no = int(input("\nEnter the Number : "))
        lst.append(no)
        i += 1

    print("\nEntered list of number is ",lst)

    prime_list = []
    for num in lst:
        if num > 1:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_list.append(num)

    print("\nList of all Prime Numbers is:", prime_list)    

    Mdata = list(map(MULT_PRIME_BY_2,prime_list))
    print("\nAfter multiplying prime numbers by 2 : ",Mdata)

    Rdata = reduce(MAX_OF_MAP_LIST,Mdata)
    print("\nMaximum of all Squares ",Rdata)


if __name__ =='__main__':
    main()