class Bookstore :
    No_Of_Books = 0

    def __init__(self):
        self.Name   = input("Enter the name of Name of Book : ")
        self.Author = input("Enter name of Author :")
        Bookstore.No_Of_Books = Bookstore.No_Of_Books + 1

    def Display(self):
        print(self.Name,"by",self.Author,"No of Books : ",Bookstore.No_Of_Books)

obj = Bookstore()
obj.Display()

obj2 = Bookstore()
obj2.Display()
    