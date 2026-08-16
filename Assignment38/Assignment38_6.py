import os
import time
import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 60

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 3")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 3")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    Total_students = df.shape[0]

    studyhrs_list = []
    Study_hrs = df["StudyHours"]
    for i in Study_hrs:
        studyhrs_list.append(i)

    plt.figure(figsize=(7,5))
    plt.hist(studyhrs_list,bins=5,color="purple",edgecolor="red")
    plt.title("Histogram of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    #plt.grid()
    plt.show()

    print("\nHistogram is closed")
        
if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	