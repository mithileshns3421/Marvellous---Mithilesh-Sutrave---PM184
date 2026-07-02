def print_number_in_reverse(no):
    list = []
    for i in range(1,no+1):       
        list.append(i)
        
    list.reverse()
    print("Reverse Order till given number using List is :-",list)
    print("\n")

    for i in range(no,0,-1):
        print("Reverse Order till given number using for loop is :-",i)


def main():
    a = int(input("\nEnter the Number :- "))
    print_number_in_reverse(a)

if __name__ == "__main__":
    main()