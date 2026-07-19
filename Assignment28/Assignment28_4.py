import sys 
def main():
    try:

        if (len(sys.argv) != 3) :
            print("Insufficient Arguments..")
            return 0 

        No1 = sys.argv[1]
        No2 = sys.argv[2]
            
            
        cnt = 0
        fobj = open(No1,'r')
        data = fobj.read()
        #print("Content from File 1")
        #print("-" *50)
        #print(data)

        fobj1 = open(No2,'w')
        data1 = fobj1.write(data)
        print()
        print(f"Contents of {No1} copied successfully into {No2}")


    except FileNotFoundError as fobj:
       print("File not found in current directory.")


if __name__ == "__main__":
    main()