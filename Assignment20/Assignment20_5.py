import threading
import time

def small(Data):
    print(f"\nTHREAD NAME : small started at {time.perf_counter() } ")
    print("\nTID of small is :",threading.get_ident())
    s = 0
    for ch in Data:
        if 'a' <= ch <= 'z':
            s = s + 1

    print("Total Small letters are : ",s)
    

def capital(Data):
    print(f"\nTHREAD NAME : capital started at {time.perf_counter() } ")
    print("\nTID of capital is :",threading.get_ident())
    c = 0
    for ch in Data:
        if 'A' <= ch <= 'Z':
            c = c + 1

    print("Total Capital letters are : ",c)
    

def countdigit(Data):
    print(f"\nTHREAD NAME : count started at {time.perf_counter() } ")
    print("\nTID of count is :",threading.get_ident())

    d = 0
    for ch in Data:
        if '0' <= ch <= '9':
            d = d + 1
    
    print("Total Digits are : ",d)


def main():

    no = input("\nEnter the string in Small/Capital/Integer format : ")
    #threads Created.

    t1 = threading.Thread(target=small,args=(no,))
    t2 = threading.Thread(target=capital,args=(no,))
    t3 = threading.Thread(target=countdigit,args=(no,))

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()

    print("\nExit from Main")

if __name__ == '__main__':
    main()