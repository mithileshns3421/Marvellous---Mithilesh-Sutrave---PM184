import sys 
def main():
    try:

        if (len(sys.argv) != 3) :
            print("Insufficient Arguments..")
            return 0 

        Fname = sys.argv[1]
        Word  = sys.argv[2]            
            
        found = 0
        fobj = open(Fname,'r')
        for i in fobj:
            if Word in i.split(): 
                found = 1
        
            
        if found == 1:
            print(f"\nEntered word {Word} FOUND in {Fname}") 
        else:
            print(f"\nEntered word {Word} NOT FOUND in {Fname}")
        
    except FileNotFoundError as fobj:
       print("File not found in current directory.")


if __name__ == "__main__":
    main()