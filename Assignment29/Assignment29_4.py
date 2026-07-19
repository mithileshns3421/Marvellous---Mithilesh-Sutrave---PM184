import sys
import os

def main():
    try:
        if (len(sys.argv) != 3) :
            print("Insufficient Arguments..")
            return 0 

        Fname     = sys.argv[1]
        New_Fname = sys.argv[2]

        if os.path.exists(Fname):
            print(f"\nFile {Fname} exists.")
        else:
            print(f"\nFile {Fname} does not exists.")

        if os.path.exists(New_Fname):
            print(f"\nFile {New_Fname} exists.")
        else:
            print(f"\nFile {New_Fname} does not exists.")
            nfobj = open(New_Fname,'w')
            print(f"\nAs file was not present, new file {New_Fname} is created.")

        fobj = open(Fname,"r")
        data = fobj.read()

        fobj1 = open(New_Fname,'r')
        data1 = fobj1.read()

        if data == data1:
            print("\nSuccess")
        else:
            print("\nFailure") 


    except FileNotFoundError as fobj:
        print("File not found in current directory.")



if __name__ == "__main__":
    main()