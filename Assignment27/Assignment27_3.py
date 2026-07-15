class Number:
    pass
    
    def __init__(self):
        self.no = int(input("\nEnter the number : "))
        Number.Value = 1

    def CheckPrime(self):
        if self.no < 1:
            print(f"\nGiven number {self.no} is not a Prime Number")
        else:
            is_prime = True

            for i in range(2,int(self.no ** 0.5)+1):
                if self.no % i == 0 :
                    is_prime = False
                    print(f"\nGiven number {self.no} is not a Prime Number")

            if is_prime:
                print(f"\nGiven number {self.no} is a Prime Number")

    def CheckPerfect(self):
        self.sum = 0
        for i in range(1,self.no):
            if self.no % i == 0 :
                self.sum = self.sum + i

        if self.sum == self.no:
            print(f"\nGiven number {self.no} is a perfect Number")
        else:
            print(f"\nGiven number {self.no} is not a perfect Number")

    def CheckFactors(self):
        print()
        for i in range(1,self.no+1):
            if self.no%i == 0:
                print(f"Factors for Given number {self.no} are :",i)

    def Sum_of_Factors(self):
        print()
        self.sof = 0
        for i in range(1,self.no+1):
            if self.no%i == 0:
                self.sof += i

        print("\nSum of All Factors is :",self.sof)


obj = Number()
obj.CheckPrime()
obj.CheckPerfect()
obj.CheckFactors()
obj.Sum_of_Factors()