import threading

def sum_of_element(Data):
    sum = 0
    for i in Data:
        sum = sum + i

    print("\nSum of all the elements is : ",sum)    

def product_of_element(Data):
    prod = 1
    for i in Data:
        prod = prod * i

    print("Product of all the elements is : ",prod)


def main():

    inp_list = list(map(int,input("\nEnter numbers separated by comma: ").split(',')))
    print("\nEntered List is : ",inp_list)

    t1 = threading.Thread(target=sum_of_element,args=(inp_list,))
    t2 = threading.Thread(target=product_of_element,args=(inp_list,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()