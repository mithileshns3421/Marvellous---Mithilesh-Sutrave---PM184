import os
import time
import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 60

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 9")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 9")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    Total_students = df.shape[0]

    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["AssignmentsCompleted"],temp["FinalResult"],label = sp)

   # plt.scatter(["AssignmentsCompleted"],["FinalResult"])
    plt.title("Comparisn")

    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")

    plt.legend()
    plt.grid(True)
    plt.show()

    print("\nHistogram is closed")
        
if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	