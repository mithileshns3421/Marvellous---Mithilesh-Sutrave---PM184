

def display_grade(a):
    if a < 50:
        print("Fail")
    elif a >= 50 and a < 60:
        print("Second Class")
    elif a >= 60 and a < 75:
        print("First Class")
    else:
        print("Distinction")    



def main():
    marks = int(input("\nEnter the Marks := "))
    display_grade(marks)


if __name__ == "__main__":
    main()