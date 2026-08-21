import pandas as pd
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
# Calculating the average by grouping the male and female
########################################################

    average_marks=df.groupby("Gender")[["Math","Science","English"]].mean()
    print("\nAverage marks according to gender are : \n ",average_marks)
    

if __name__=="__main__":
    main()