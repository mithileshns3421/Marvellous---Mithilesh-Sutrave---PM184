def area_of_circle(a):
    pi = 3.14
    areac = pi * a * a
    print("\nArea of Circle is :- ", int(areac))

def main():
    a = int(input("\nEnter the radious to calculate diameter of circle :- "))
    area_of_circle(a)

if __name__ == "__main__":
    main()