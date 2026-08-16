import os
import time
import pandas as pd

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
    Study_Hours = df["StudyHours"]
    Total_study_hours = sum(Study_Hours)
    avg_study_hrs = Total_study_hours/Total_students

    Present = df["Attendance"]
    Total_Present = sum(Present)
    avg_attendance = Total_Present/Total_students

    Pre_Score = df["PreviousScore"]
    Sleep_hrs = df["SleepHours"]

    Max_Previos_Score = max(Pre_Score)
    Min_Sleep_Hours = min(Sleep_hrs)

    print(f"\nAverage Study Hours of Class is    : {int(avg_study_hrs)} Hrs.")    
    print(f"\nAverage Attendance of Class is     : {int(avg_attendance)} Days.")    
    print(f"\nMaximum Previous Score of Class is : {int(Max_Previos_Score)}.")    
    print(f"\nMinimum Sleep Hours of Class is    : {int(Min_Sleep_Hours)} Hrs.")    

    


if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	