# What does the id() function return?
# Is the value returned by id() same for two variables holding the same value?
print("ID() function returns the memory address of the value assigned to variable.")
print("During runtime if it is found that variable holds the same value in case of INT and STR then the value returned by ID() will be same")
print("\nExample")
a = 'Mithilesh' 
b = 'Mithilesh'
print("Value of a ",a)
print("Value of b ",b)
#print("\n")
print("Memory address of a ",id(a))
print("Memory address of b ",id(b))
#print("\n")
print("Yes, Value retuned by id() is SAME for 2 variables holdingsame value in case if STR & INT ")

print("But Value retuned by id() is NOT SAME for 2 variables holdingsame value in case if LIST, Example given below. ")

list1 = [10,20]
list2 = [10,20]

print("List 1",list1)
print("List 2",list2)
print("\n")
print("Memory address of List 1 ",id(list1))
print("Memory address of List 2 ",id(list2))
print("\nAs above 2 memory address are different for list, so it will not hold same in case of LIST")

