class Arithmetic:
    pass

    def __init__(self):
        self.no1 = 0
        self.no2 = 0

    def Accept(self):
        self.no1 = int(input("Enter first  Number: "))
        self.no2 = int(input("Enter second Number: "))

    def Addition(self):
        return self.no1 + self.no2

    def Substraction(self):
        return self.no1 - self.no2

    def Multiplication(self):
        return self.no1 * self.no2

    def Division(self):
        try:
            return self.no1 / self.no2
        except ZeroDivisionError as zobj:
            print("\nException occured due to Second operand is zero : ",zobj)

        
obj = Arithmetic()
obj.Accept()

addn = obj.Addition()
print("\nAddition is       : ",addn)

subn = obj.Substraction()
print("Substraction is   : ",subn)

muln = obj.Multiplication()
print("Multiplication is : ",muln)

divn = obj.Division()
print("Division is       : ",divn)
