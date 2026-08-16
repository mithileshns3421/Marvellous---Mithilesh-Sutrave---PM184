import os
import time
import pandas as pd

Border = "-" * 50

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 1")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 1")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)
    print("\nDataset Loaded Succesfully.")

    print("\nFirst 5 records are :");
    print(df.head())
    print("\nLast  5 records are :");
    print(df.tail())
    print("\nTotal number of Rows and Columns are :")
    print(df.shape)
    print("\nList of Column Names are :")
    print(list(df.columns))
    print("\nDatatype of Each column is : ")
    for i in (list(df.columns)):
        print("Column",i,':',type(i))


if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	