import sys
import os

def main():
    try:
        if (len(sys.argv) != 2) :
            print("Insufficient Arguments..")
            return 0 

        Fname = sys.argv[1]

        if os.path.exists(Fname):
            print(f"\n{Fname} exists.")
        else:
            print(f"\n{Fname} does not exists.")

    except FileNotFoundError as fobj:
        print("File not found in current directory.")



if __name__ == "__main__":
    main()