import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def main():

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


    print("\nGraphical representation of marks for Sagar is : ")

    dfa=df.set_index("Name")
    sagar_marks=dfa.loc["Sagar"].drop("Gender")
    sagar_marks.plot(kind="line",marker="o",title="Sagar marks ")

    plt.show()
    



    


if __name__=="__main__":
    main()