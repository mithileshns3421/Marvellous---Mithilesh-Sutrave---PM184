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
    print("Dataframe is :")
    print(df)
      

########################################################
# Adding Status column 
########################################################

    df["Total"]=df["Math"]+df["Science"]+df["English"]

    df["Status"]=np.where(df["Total"]>250,"Pass","Fail")
    print("\nAfter adding status column : ")
    print(df)
    
########################################################
# Renaming Math column
########################################################

    df=df.rename(columns={"Math":"Mathematics"})
    print("\nAfter renaming : ")
    print(df)
    

if __name__=="__main__":
    main()