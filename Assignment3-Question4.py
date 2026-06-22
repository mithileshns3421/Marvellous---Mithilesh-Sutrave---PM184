def fun():
    x = 10
    print(x)

fun()
print("Here, above we have called a Function fun() which has value 10 assigned to x \nand it is shown as output.")
print("\n")

print("**********Program for default return value of a function.**********")
def add(a, b):
    c = int(a) + int(b)
    return c

result = int(add(input("Enter 1st No :- "), input("Enter 2nd No :- ")))
print("\nAddition Result - ",result)
print("Here, above we have called a Function add() which will always required 2 input values a and b;\nwhich will add and output will be returned using RETURN keyword.")
