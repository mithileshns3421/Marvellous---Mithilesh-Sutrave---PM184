from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pandas as pd

def main():
    X=[[25,20000],
       [30,40000],
       [35,80000]]

    print("\nBefore feature scaling :")
    print(X)
    
    scalar=MinMaxScaler()
    X=scalar.fit_transform(X)
    print("\nAfter feature scaling : ")
    print(X)


if __name__=="__main__":
    main()