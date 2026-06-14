#difference between 
a = 10
b = 10

print("Value of a is ",a)
print("Value of b is ",b)
print("Shown above  values of a&b are integer which will hold the SAME MEMORY ADDRESS")
print("Memory address of a",id(a))
print("Memory address of b",id(b))

a = [10]
b = [10]

print("Value of a is ",a)
print("Value of b is ",b)
print("Shown above  values of a&b are list which will hold DIFFERENT MEMORY ADDRESS")
print("Memory address of a",id(a))
print("Memory address of b",id(b))


print("However I tried to check first value from the list and found it holds the same value.")
print("First value from list a",id(a[0]))
print("First value from list b",id(b[0]))

