import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    # Create dataset
    data = {
        "StudyHours": [1, 2, 3, 4, 5],
        "SleepHours": [7, 6, 7, 6, 8],
        "Marks": [50, 55, 60, 65, 70]
    }

    df = pd.DataFrame(data)

    X = df[["StudyHours", "SleepHours"]]

    Y = df["Marks"]

    model = LinearRegression()

    model.fit(X,Y)

    # Print coefficients
    print("\nCoefficient for StudyHours:", model.coef_[0])
    print("\nCoefficient for SleepHours:", model.coef_[1])

    # Print intercept
    print("\nIntercept:", model.intercept_)

if __name__=="__main__":
    main()