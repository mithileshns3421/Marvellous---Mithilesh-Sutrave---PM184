import numpy as np

def main():
    X=[6,7,8,9,10,11,12]
    X_var=np.var(X)
    print("\nGive DataSet is :",X)
    print("\nVariance is :",X_var)
    X_standard=np.std(X)
    print("\nStandard is :",X_standard)
    

if __name__=="__main__":
    main()