import sys
print("\n****************** USE CASE for List and Tuple ******************")
lst = [1,2,3,4]
tup = (1,2,3,4)

print("Give is the List  :",lst)
print("Lists are always given in SQUARE BRACKETS ")
print("Type of Above is  :",type(lst))
print(id(lst))
print("Size if list is : ",sys.getsizeof(lst))

print("\nGive is the Tuple :",lst)
print("Tuples are always given in ROUND BRACKETS ")
print("Type of Above is  :",type(tup))
print(id(tup))
print("Size if list is : ",sys.getsizeof(tup))
