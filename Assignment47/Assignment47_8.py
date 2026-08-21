import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def main():

    StudyHours=np.array([[1],[2],[3],[4],[5]])
    Marks=np.array([50,55,60,65,70])

    predict=[[6]]

    model=LinearRegression()

    model=model.fit(StudyHours,Marks)
    Y_pred=model.predict(predict)

    print("\nPredicted value is :",Y_pred)
    print("\nCoefficient is     :",model.coef_)
    print("\nIntercept is       :",model.intercept_)

if __name__=="__main__":
    main()