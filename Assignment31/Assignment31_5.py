import datetime
import schedule
import time
import os

def DirScan(Dname):

    logfilename = datetime.datetime.now().strftime("DirectoryCountLog_%d%m%Y_%H%M%S.txt") 
    filecnt = 0
     
    fobj = open(logfilename,'w')
    fobj.write("*" * 100 + "\n")
    fobj.write(f"Details in the directory are noted on : {time.ctime()}\n\n")
    fobj.write("*" * 100 + "\n\n")

    abs_path = os.path.abspath(Dname)           # get the absolute path
    rel_path = os.path.relpath(Dname)           # get the relative path , ( we get only folder name here )

    for Foldername,Subfolder,filename in os.walk(Dname):
        for fname in filename:
            filecnt = filecnt + 1

        fobj.write(f"Directory Path : {abs_path}\n")
        fobj.write(f"Relative  Path : {rel_path}\n")

        fobj.write("Number of files : " + str(filecnt) + "\n")
        fobj.write(f"Date and Time  : {datetime.datetime.now()}\n")
        

    fobj.close()

    print(f"\nLog file {logfilename} created and details added successfully.")


def main():
    Dirname = input("\nEnter the Directory name : ")
    ret = False
    ret = os.path.exists(Dirname)
    dir_name = os.path.basename(Dirname)

    if ret == False:
        print(f"\nMarvellous Automation Error : No such directory is present with name -> {dir_name} .")
        return

    schedule.every(5).minutes.do(DirScan,dir_name)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

