import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

Border = "-" * 60

def top():
    print()
    print(Border)
    print("         Student Performance Case Study Question 10")
    print("         Started  at :",time.ctime())
    print(Border)

def bottom():
    print()
    print(Border)
    print("         End of Student Performance Case Study Question 10")
    print("         Finished at :",time.ctime())
    print(Border)

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    # X = Independent Variables (Features)
    # Y = Dependent Variables   (Labels)

    feature_cols = [
                "StudyHours",
                "Attendance",
                "PreviousScore",
                "AssignmentsCompleted",
                "SleepHours",
                ]

    X = df [feature_cols]
    Y = df ["FinalResult"]

    print()
    print("X Shape : ",X.shape)
    print("Y Shape : ",Y.shape)

    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)  #shuffling starts here

    print("\nDataset Splitting Activity Done.")

    print("X : ", X.shape) #output [150,4]
    print("Y : ", Y.shape) #output [150,] 
    print()
    print("X_Train :",x_train.shape)    #output (75,4)
    print("X_Test  :",x_test.shape)     #output (75,4)
    print("Y_Train :",y_train.shape)    #output (75,)
    print("Y_Test  :",y_test.shape)     #output (75,)

    model = DecisionTreeClassifier(max_depth=3)
    print("\nModel gets created successfully.")

    model = model.fit(x_train, y_train)
    y_train_pred = model.predict(x_train)

    train_accuracy = accuracy_score(y_train, y_train_pred)

    print("\nTraining Accuracy ---------> : {:.2f}%".format(train_accuracy * 100))

    y_pred = model.predict(x_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    print("\nTesting Accuracy ----------> : {:.2f}%".format(test_accuracy * 100))

    difference = train_accuracy - test_accuracy

    if difference > 0.15:
        print("\nObservation : Model is Overfitting.")

    elif train_accuracy < 0.70 and test_accuracy < 0.70:
        print("\nObservation : Model is Underfitting.")

    else:
        print("\nObservation : Model is performing reasonably well.")

if __name__== "__main__":    
    os.system("cls")
    top()
    main()
    bottom()
	