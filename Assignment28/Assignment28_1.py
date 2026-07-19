import sys

def main():
    try:
        if (len(sys.argv) != 2):
            print("\nInsufficient Arguments.")
            return 0

        No1 = sys.argv[1]

        cnt = 0
        #fname = input("Enter the file name you want to count the lines for : ")

        fobj = open(No1,'r')

        with fobj as line:
            for l in line:
                cnt = cnt + 1

        print(f"\nTotal number of lines in this file {No1} is : ",cnt)

        fobj.close()

    except FileNotFoundError as fobj:
       print("File not found in current directory.")


if __name__ == "__main__":
    main()