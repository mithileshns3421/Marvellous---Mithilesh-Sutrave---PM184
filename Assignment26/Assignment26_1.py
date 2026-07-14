class Demo():
    Value = 100

    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b

    def Fun(self):
        print("\nInside Instance Method named as Fun.")
        print("Instance Variable NO1 :- ",self.no1)
        print("Instance Variable NO2 :- ",self.no2)

    def Gun(self):
        print("\nInside Instance Method named as Gun.")
        print("Instance Variable NO1 :- ",self.no1)
        print("Instance Variable NO2 :- ",self.no2)
        print("\nValue for Class variable is : ",Demo.Value)    

a = int(input("enter the First  value :"))
b = int(input("enter the Second value :"))

Obj1 = Demo(a,b)
Obj2 = Demo(a,b)

Obj1.Fun()
Obj2.Fun()

Obj1.Gun()
Obj2.Gun()


