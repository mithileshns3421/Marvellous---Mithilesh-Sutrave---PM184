import sys
import os

def main():
    try:
        if (len(sys.argv) != 2) :
            print("Insufficient Arguments..")
            return 0 

        Fname = sys.argv[1]

        if os.path.exists(Fname):
            print(f"\nFile {Fname} exists.")
        else:
            print(f"\nFile {Fname} does not exists.")

        print("*" * 80)    

        fobj = open(Fname,"r")
        data = fobj.read()

        print("\nContent of file")
        print(data)
        print()
        print("*" * 80)    

    except FileNotFoundError as fobj:
        print("File not found in current directory.")



if __name__ == "__main__":
    main()