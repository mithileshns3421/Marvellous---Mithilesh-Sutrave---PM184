import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def main():
    
############################################
# Load the Data
############################################
    
    print("\nLoad the Data")
    
    Datapath="Advertising.csv"
    df=pd.read_csv(Datapath)
    print(df.head())
    print("\nData loaded successfully")

############################################
# Handling mising values 
############################################
    
    print("\nHandling mising values")    

    print("\nTotal mising values : ",df.isnull().sum())
    df=df.drop(columns=["Unnamed: 0"])
    print("\nDataset after removing unnamed column is : ")
    print(df.head())

############################################
# Spliting of Independent and dependent variables 
############################################
    
    print("\nSpliting of Independent and dependent variables")    

    X=df[["TV","radio","newspaper",]]
    Y=df["sales"]

    print("\nIndependent variables :")
    print(X.head())

    print("\nDependent variables is :")
    print(Y.head())

############################################
# split the Dataset
############################################
    
    print("\nSplit the Dataset")
    
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.3)

    print("\nTraining Dataset :",X_train.head())
    print("\nTesting Dataset :",X_test.head())
    print("\nSpliting of Dataset done ")

############################################
# Train and Test the model
############################################
    
    print("\nTrain and Test the model")
    
    model=LinearRegression()
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)

    print("\nExpected answer : ")
    print(list(Y_test))
    print("\nPredicted answer : ")
    print(Y_pred)

############################################
# Evaluate the model
############################################
    
    print("\nEvaluate the model")
    
    MSE=mean_squared_error(Y_test,Y_pred)
    RMSE=np.sqrt(MSE)
    R2=r2_score(Y_test,Y_pred)
    print("\nMean squared error is :",MSE)
    print("\nRoot Mean squared error is :",RMSE)
    print("\nR2_score value : ",R2)

    

if __name__=="__main__":
    main()