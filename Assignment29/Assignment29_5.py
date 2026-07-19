import sys
import os

def main():
    try:
        if (len(sys.argv) != 3) :
            print("Insufficient Arguments..")
            return 0 

        Fname = sys.argv[1]
        Word  = sys.argv[2]
        cnt = 0

        if os.path.exists(Fname):
            print(f"\nFile {Fname} exists.")
        else:
            print(f"\nFile {Fname} does not exists.")

        fobj = open(Fname,"r")
        for i in fobj:
            words = i.split()
            
            for j in words:
                if j == Word:
                    cnt = cnt + 1  
            

        print(f"\nGiven word {Word} is {cnt} times.")

    except FileNotFoundError as fobj:
        print("File not found in current directory.")


if __name__ == "__main__":
    main()