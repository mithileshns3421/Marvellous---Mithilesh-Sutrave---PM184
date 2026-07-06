def print_star(a):
    print('*' * a )
def main():
    print("\nProgram which accept number from user and print that number of “*” on screen")
    no = int(input("\nEnter the number you want to print * : "))
    print_star(no)
    
    
if  __name__ == "__main__":
    main()