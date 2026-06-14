#a = 10
#b = 10
#print(id(a) == id(b))
#Explain why this happens.

a = 10
b = 10

print("Value of a is",a)
print("Value of b is",b)

print("Since a and b hold same value which also means same datatype(INT), hence it will hold same memory")
print("SO,id(a) will be same as id(b), Shown Below.")

print(id(a))
print(id(b))

print("Now as it holds the same memroy address, the output of given question will be TRUE")
print("id(a) == id(b)--->",id(a) == id(b))