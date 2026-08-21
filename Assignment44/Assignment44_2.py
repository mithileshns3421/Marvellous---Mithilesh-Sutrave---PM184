import pandas as pd


def main():

    Border="*"*80

    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82]
    }

    df = pd.DataFrame(Data)
    print(Border)
    print("\nShape of dataframe is:",df.shape)
    print()
    print(Border)
    print("\nColumn of dataframe is :",list(df.columns))
    print()
    print(Border)
    print("\nData type : ",type(df))
    print()
    print(Border)

    ########################################################
    # Description of Data
    ########################################################

    print("\nDescription is :\n")
    print(df.describe())
    print()
    print(Border)

if __name__=="__main__":
    main()