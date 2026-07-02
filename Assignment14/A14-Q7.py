def main():
    print("\nlambda function which accepts one number and returns True if divisible by 5.")
    check_div_by_5 = lambda no : no % 5 == 0

    no = int(input("\nEnter the Number :"))

    res = check_div_by_5(no)
    if res == True :
        print("\nGiven number",no,"Is divisible of 5.")


if __name__ == '__main__':
    main()