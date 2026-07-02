def sum_of_given_number(a):
    cnt = 0
    for i in range(a+1):
        cnt = cnt + i

    return cnt    
    #print("Sum of first Natural Numbers starting from 0/1 is :- ",cnt)

def main():
    a = int(input("Enter the number :- "))
    cnt = sum_of_given_number(a)
    print("Sum of first Natural Numbers starting from 0/1 is :- ",cnt)    

if __name__ ==  "__main__":
    main()