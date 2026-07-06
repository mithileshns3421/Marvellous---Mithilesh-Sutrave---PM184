import threading
import time

def Evenlist(Data):
    emp_even_list = []
    sum = 0
    for i in Data:
        if i%2 == 0:
           emp_even_list.append(i)
           sum = sum + i

    print("\nEven List is : ",emp_even_list)
    print("Sum of Evenlist is : ",sum)
    print(f"Exit from Evenlist.")

def Oddlist(Data):
    emp_odd_list = []
    sum1 = 0
    for i in Data:
        if i%2 != 0:
            emp_odd_list.append(i)
            sum1 = sum1 + i

    print("\nOdd List is : ",emp_odd_list)
    print("Sum of Oddlist is : ",sum1)
    print(f"Exit from Oddlist.")


def main():

    inp_list = list(map(int,input("Enter numbers separated by comma: ").split(',')))
    print("Entered List is : ",inp_list)

    #threads Created.
    t1 = threading.Thread(target=Evenlist,args=(inp_list,))
    t2 = threading.Thread(target=Oddlist,args=(inp_list,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()