def calc_length(a):
    res = len(a)

def main():

    name = input(("\nWrite a string you want to find the length."))
    b = calc_length(name)
    print("Length of given String",name," is : ",b)
    
if  __name__ == "__main__":
    main()