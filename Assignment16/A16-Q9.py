#Just to have practice of both while and for loop , below two programs are written.


def first_10_even():
    i = 1
    for i in range(1,21):
        if i%2 == 0:
            print(i,end="," if i != 20 else "")

def first_10_odd():
    count = 1
    num = 1
    while count <= 10:
        print(num, end="," if num != 19 else "")
        num += 2
        count += 1 


def main():

    print("\nWrite a program which display first 10 even numbers on screen")
    first_10_even() 
    print("\n")   
    first_10_odd()
if  __name__ == "__main__":
    main()