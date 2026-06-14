#Predict the output:

x = input("Enter Number: ")
print(type(x))

print("Here entered number will give the output as its original Type. Input is string as explicit conversion is not happening and input function will treat it as string.")

x = int(input("\nEnter number again which will explicitely convert the number in INT : "))
print(type(x))
