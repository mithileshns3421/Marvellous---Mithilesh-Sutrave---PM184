import threading

def max_list_element(Data):
    res = max(Data)
    print("Maximum element from the given list is :",res)    

def min_list_element(Data):
    min_el = min(Data)
    print("Minimum element from the given list is :",min_el)



def main():

    inp_list = list(map(int,input("Enter numbers separated by comma: ").split(',')))
    print("Entered List is : ",inp_list)

    t1 = threading.Thread(target=max_list_element,args=(inp_list,))
    t2 = threading.Thread(target=min_list_element,args=(inp_list,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()