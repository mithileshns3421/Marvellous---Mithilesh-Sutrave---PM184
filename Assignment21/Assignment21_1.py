import threading
import time

def prime(Data):
    prime_list = []
    print(f"\nTHREAD NAME : PRIME started at {time.perf_counter() } ")
    
    for num in Data:
        if num > 1:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_list.append(num)

    print("Prime Numbers:", prime_list)


def non_prime(Data):
    print(f"\nTHREAD NAME : non prime started at {time.perf_counter() } ")
    non_prime_list = []
    print(f"\nTHREAD NAME : PRIME started at {time.perf_counter() } ")
    
    for num in Data:
        if num >= 1:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if not is_prime:
                non_prime_list.append(num)

    print("Non Prime Numbers:", non_prime_list)
    


def main():

    inp_list = list(map(int,input("Enter numbers separated by comma: ").split(',')))
    print("Entered List is : ",inp_list)

    t1 = threading.Thread(target=prime,args=(inp_list,))
    t2 = threading.Thread(target=non_prime,args=(inp_list,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()