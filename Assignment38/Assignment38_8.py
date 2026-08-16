import os
import time
import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 60

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 8")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 8")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    Q1 = df["Attendance"].quantile(0.25)
    Q3 = df["Attendance"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df["Attendance"] < lower_limit) |
        (df["Attendance"] > upper_limit)
    ]

    print("Lower Limit :", lower_limit)
    print("Upper Limit :", upper_limit)

    print("\nOutliers:")
    print(outliers)


    plt.figure(figsize=(7,5))

    plt.boxplot(df["Attendance"])
    plt.title("Boxplot for Attendance")
    plt.ylabel("Attendance")

    plt.show()
    print("\nBoxPlot is closed")
        
if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	