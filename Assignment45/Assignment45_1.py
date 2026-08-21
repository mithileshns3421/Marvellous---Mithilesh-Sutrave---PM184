import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():

    Border= "*" * 80

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
    # Performing the Min Max scaling
    ########################################################

    scalar=MinMaxScaler()
    df["Math"]=scalar.fit_transform(df[["Math"]])
    print("\nAfter Min Max scaling considering values of Math : ")
    print(df)

'''
    print("\nAfter Min Max scaling considering values of Science: ")
    df["Science"] = scalar.fit_transform(df[["Science"]])
    print(df)    

    print("\nAfter Min Max scaling considering values of English: ")
    df["English"] = scalar.fit_transform(df[["English"]])
    print(df)    
'''

if __name__=="__main__":
    main()