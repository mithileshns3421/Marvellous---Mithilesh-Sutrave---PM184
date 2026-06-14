#Write a program to take user’s name and age and display:
#Hello <name>, you will turn <age+1> next year.

name = input("Enter your name: ")
age  = int(input("Enter your age: "))

print("\nHello",name,"you will turn",age+1,"next year.")

print("\nIt is understood that, during input of age it is important that we have to use Explicit Conversion.\nOtherwise age+1 will not work and will give error.")

