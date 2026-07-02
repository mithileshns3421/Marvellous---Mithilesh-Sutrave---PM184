def chk_div_by_3(a):
    if a%3==0 & a%5==0:
        print("\nDivisible by 3 & 5 both.")
    else:
        print("\nCannot by divided by 3 & 5 both.")

def main():
    No1 = int(input("\nEnter the Number :- "))
    chk_div_by_3(No1)

if __name__ == "__main__":
    main()