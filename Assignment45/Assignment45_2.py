import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def main():

    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82]        
    }

    df=pd.DataFrame(Data)
    print("\nDataframe is :")
    print(df)

########################################################
# Encoding the Gender column 
########################################################

    df["Gender"]=["Male","Male","Female"]
    
    print("\nBefore encoding :")
    print(df)
    print("\nAfter encoding :")
    df_encoded=pd.get_dummies(df,columns=["Gender"])
#    df_encoded=pd.get_dummies(df,columns=["Gender"],dtype=int)
    print(df_encoded) 


if __name__=="__main__":
    main()