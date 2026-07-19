import sys

def main():
    try:
        if (len(sys.argv) != 2):
            print("\nInsufficient Arguments.")
            return 0
    
        No1 = sys.argv[1]

        cnt = 0
        #fname = input("Enter the file name : ")

        fobj = open(No1,'r')
        data = fobj.read()
        
        print("\n************ File contains the data as show below ************")
        print()
        print(data) 

    except FileNotFoundError as fobj:
       print("File not found in current directory.")


if __name__ == "__main__":
    main()