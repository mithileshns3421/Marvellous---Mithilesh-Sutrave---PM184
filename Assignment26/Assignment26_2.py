class Circle:
    # Class variable
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter the value of Radius: "))

    # Calculate Area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate Circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display details
    def Display(self):
        print("\nEntered Radius is           :", self.Radius)
        print("Area of Circle is           :", self.Area)
        print("Circumference of Circle is  :", self.Circumference)

print()
print("*" * 80)
print("Circle 1")
obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()


print("*" * 80)
print("\nCircle 2")
obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
print("*" * 80)
