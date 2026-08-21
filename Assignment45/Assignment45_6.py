import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def main():
########################################################
# Load The Data
########################################################

    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82],
        
    }

    
    df=pd.DataFrame(Data)
    print("\nDataframe is :")
    print(df)
    
    
########################################################
# Encoding the Gender Column
########################################################

    df["Gender"]=["Male","Male","Female"]
    print("\nBefore encoding :")
    print(df)
    

    print("\nAfter encoding :")
    df_encoded=pd.get_dummies(df,columns=["Gender"])
    print(df_encoded)
    
########################################################
# Calculating average by grouping male and Female
########################################################

    average_marks=df.groupby("Gender")[["Math","Science","English"]].mean()
    print("\nAverage marks according to gender are : \n ",average_marks)
    
########################################################
# Graphical Representation
########################################################


    print("\nGraphical representation of sagar vs marks is : ")
    dfa=df.set_index("Name")
    sagar_marks=dfa.loc["Sagar"].drop("Gender")
    sagar_marks.plot(kind="line",marker="o",title="Sagar marks ")
    plt.show()
    

########################################################
# Adding Status column 
########################################################

    df["Total"]=df["Math"]+df["Science"]+df["English"]

    df["Status"] = np.where (df["Total"]>250,"Pass","Fail")
    print("\nAfter adding status column : ")
    print(df)
    
########################################################
# Counting the Pass and Fail students 
########################################################

    count=df["Status"].value_counts()
    print("\nPassed students ",count.get("Pass"))
    print("\nFailed students ",count.get("Fail"))

if __name__=="__main__":
    main()