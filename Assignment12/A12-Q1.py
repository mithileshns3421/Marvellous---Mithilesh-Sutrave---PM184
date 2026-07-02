def check_vovel(input_string):
    if input_string in 'aeiou' or input_string in 'AEIOU':
        print("\nEntered character",input_string,"is a Vovel.")
    else:
        print("\nEntered character",input_string,"is not a Vovel.")


def main():
    a = input("\nEnter the character to check if it is vovels :- ")
    check_vovel(a)

if __name__ == "__main__":
    main()