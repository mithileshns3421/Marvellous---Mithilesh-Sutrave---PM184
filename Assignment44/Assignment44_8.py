import pandas as pd
import matplotlib.pyplot as plt

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
    print()
    print("Shape of dataframe is:",df.shape)
    print()
    print(Border)

    print("\nColumn of dataframe is :",list(df.columns))
    print("\nData type : ",type(df))
    print("\nDescription is :")
    print(df.describe())
    print()
    print(Border)
    print()
    df["Total"]=df["Math"]+df["Science"]+df["English"]
    print("\nNew column named Total is :\n ", df["Total"])
    print()
    print(Border)

    print("\nMarks greater than 85 in science are : ")
    print(df[df["Science"]>85])
    print(Border)

    df["Name"]=df["Name"].replace({"Pooja":"Puja"})
    print("\nPooja Name changed ")
    print(list(df["Name"]))
    print(Border)
    print("\nSorted Data is : ")
    sorted_data=df.sort_values(by="Total",ascending=False)
    print(sorted_data)
    print(Border)

    print("\nGraph representation for Student name Vs Total marks.\n")
    plt.figure(figsize=(8,6))
    plt.bar(df["Name"],df["Total"])
    plt.xlabel("Student Name ")
    plt.ylabel("Total marks ")
    plt.grid(True)

    plt.show()
    print(Border)
    print("Graph representation for Amit Vs Marks")
    df_Amit=df.set_index("Name")
    amit_data=df_Amit.loc["Amit"]
    amit_data.plot(kind="line",marker="o",title="Amit Data")
    plt.show()
    print(Border)
    


if __name__=="__main__":
    main()