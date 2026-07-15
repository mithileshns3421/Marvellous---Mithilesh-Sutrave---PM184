class BankAccount():
    ROI = 10.5
    Balance = 0

    def __init__(self):
        self.Name   = input("Enter the Account Holder Name : ")
        self.Initial_Amount = int(input("\nEnter Initial Amount to show the Balance :"))
        BankAccount.Balance = BankAccount.Balance + self.Initial_Amount

    def Display(self):
        print("\nAccount Name : ",self.Name)
        print("\nAccount Balance : ",BankAccount.Balance)

    def Deposit(self):
        self.Deposit_Amount = int(input("\nEnter amount to be Deposited :"))
        BankAccount.Balance = BankAccount.Balance + self.Deposit_Amount
        print("\nTotal Balance Amount : ",BankAccount.Balance)

    def Withdraw(self):
        self.Withdraw = int(input("\nEnter amount to be Withdrawn :"))
        if self.Withdraw > BankAccount.Balance:
            print("Insufficient Balance")
        else:
            BankAccount.Balance = BankAccount.Balance - self.Withdraw

        print("\nBalance Amount : ",BankAccount.Balance)    

    def CalculateInterest(self):
        self.Amount = int(input("\nEnter amount on which Interest to be calculated :"))
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        print("\nAmount of Interest Calculated is :",self.Interest)

print()
obj = BankAccount()
obj.Display()
obj.Deposit()
obj.Withdraw()
obj.CalculateInterest()

print()
obj1 = BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
print()
