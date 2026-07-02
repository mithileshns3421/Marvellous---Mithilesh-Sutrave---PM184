def tables(no1):
    tab_list = []
    for i in range(1,11):
        tab_list.append(no1*i)
        #print(no1*i)
        
    print("Multiplication table of",no1,"is:-",tab_list)
        

def main():
    a = int(input("Enter the number :- "))
    tables(a)

if __name__ ==  "__main__":
    main()