import pandas as pd
import matplotlib.pyplot as plt

def main():
    Border="*"*100
    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82],
        
    }

    df = pd.DataFrame(Data)
    print()
    print(Border)
    print("\nShape of dataframe is:",df.shape)
    print()
    print(Border)
    print("\nColumn of dataframe is :",list(df.columns))
    print()
    print(Border)
    print("\nData type :",type(df))
    print()
    print(Border)
  
    ########################################################
    # Droping the English column from Dataframe 
    ########################################################

    New_df=df.drop(columns=["English"])
    print("\nNew dataframe is : \n")
    print(New_df)
    print()

    print(Border)
    print("\nNew Columns of dataframe is :",list(New_df.columns))
    print()
    print(Border)
    

if __name__=="__main__":
    main()