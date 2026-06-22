import sys

Name = str(input("Enter the Value :- "))
print("Given input value is :- ",Name)
print('Datatype : ',type(Name))
print("Memory Address : ",id(Name))
print("Size in Bytes : ",sys.getsizeof(Name))

