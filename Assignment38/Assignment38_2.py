import os
import time
import pandas as pd

Border = "-" * 60

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 2")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 2")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("\nTotal number of students in given Dataset : ",df.shape[0])
    pass_cnt = 0 
    fail_cnt = 0
    result = df["FinalResult"]
    for i in result:
        if i == 1:
            pass_cnt = pass_cnt + 1
        else:
            fail_cnt = fail_cnt + 1

    print("\nTotal Students Passed is : ",pass_cnt)
    print("\nTotal Students Failed is : ",fail_cnt)

if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	