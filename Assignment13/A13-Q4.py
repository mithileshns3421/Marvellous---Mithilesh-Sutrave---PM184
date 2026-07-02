
def binary_equivalent(a):
    bin_val = bin(a)[2:]
    return bin_val


def main():
    a = int(input("Enter the number :- "))
    b_val = binary_equivalent(a)
    print("Binary Equivalent number is :",b_val)


if __name__ == "__main__":
    main()