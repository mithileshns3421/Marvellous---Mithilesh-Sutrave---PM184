def display_marvellous(a):
    for i in range(a):
        print("Marvellous.")


def main():
    print("\nWrite a program which display 5 times Marvellous on screen.")
    no = int(input("\nEnter how many times you want to display Marvellous : "))
    display_marvellous(no)

if  __name__ == "__main__":
    main()