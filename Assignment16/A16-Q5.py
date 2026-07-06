def display_reverse(a):
    print("\n")
    for i in range(a,0,-1):
        print(i,end="," if i != 1 else "")


def main():
    print("\nProgram which display reverse on screen")
    no = int(input("\nEnter how many numbers you want to display : "))
    display_reverse(no)
    print("\n")
if  __name__ == "__main__":
    main()