#Why does the input() function always return a string?
#How can you convert it to another data type?

print("As per understanding, input() function always returns a string because it is designed to read text entered by the user from the keyboard.\nIt gives the programmer full control over how the input should be interpreted.")

age = input("Enter your age:- ")
print(age)
print("Type of input age is ",type(age)) # here default type is STR

# We can convert the input explicitly into INT datatype using below code.

newage = int(input("Enter your age:- "))
print(newage)
print("Type of input age is ",type(newage)) # here default type is STR
