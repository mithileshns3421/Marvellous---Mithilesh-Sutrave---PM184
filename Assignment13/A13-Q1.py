def area_of_rectangle(a,b):
    arear = a * b
    print("\nArea of Rectangle is :- ", arear)

def main():
    a = int(input("\nEnter the length :- "))
    b = int(input("\nEnter the width  :- "))
    area_of_rectangle(a,b)

if __name__ == "__main__":
    main()