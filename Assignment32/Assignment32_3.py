import os
import schedule
import time

def FileDetail(fname):
    try:
        fobj = open(fname,'r')

        if not os.path.isfile(fname):
            print("\nNo such file exists.")
            return 

        #get the size of file.
        fsize = os.path.getsize(fname)

        #get the content of file and display it.    
        data = fobj.read()

        print(f"\nFile contains below data : {data} ")
        print(f"\nSize of the file is : {fsize} Bytes ")

        fobj.close()

    except FileNotFoundError as fobjnotfound:
        print("\nFile is not present in current directory.\n\n",fobjnotfound)

    except PermissionError as fobjp:
        print("\nFile doesnt have permission to access it.\n\n",fobjp)			

    except Exception as e:
        print("\nThere is an error during file operation.\n\n",e)


def main():
    fname = input("Enter the File name with path : ")
    FileDetail(fname)

    schedule.every(10).minutes.do(FileDetail,fname)

    while True:
        schedule.run_pending()
        time.sleep(1)

        
if __name__ == "__main__":
    main()