# What is the purpose of getsizeof()?
# Why is memory size different for different data types?

import sys

print("getsizeof() returns the size of an object used in bytes.")
print("It is used to find the memory size occupied by a Python object to understand how much memory an object consumes.")

a = 10
b = "Mithilesh"
c = [10,20,30]
d = (1,2,3)
e = {5,6}
print("Value of a is ",a,"              and Type is ",type(a))
print("Value of b is ",b,"       and Type is ",type(b))
print("Value of c is ",c,"    and Type is ",type(c))
print("Value of d is ",d,"       and Type is ",type(d))
print("Value of e is ",e,"          and Type is ",type(e))

print("GETSIZEOF() of a", sys.getsizeof(a))
print("GETSIZEOF() of b", sys.getsizeof(b))
print("GETSIZEOF() of c", sys.getsizeof(c))
print("GETSIZEOF() of d", sys.getsizeof(d))
print("GETSIZEOF() of e", sys.getsizeof(e))

