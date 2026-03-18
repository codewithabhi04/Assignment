class BankAccount:
    ROI = 10.5  
    
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")

    def Deposit(self, money):
        self.Amount += money
        print(f"Deposited: {money}")
        print(f"Updated Balance: {self.Amount}")

    def Withdraw(self, money):
        if money <= self.Amount:
            self.Amount -= money
            print(f"Withdrawn: {money}")
            print(f"Remaining Balance: {self.Amount}")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest: {interest}")


obj1 = BankAccount("Abhishek", 10000)

obj1.Display()
obj1.Deposit(2000)
obj1.Withdraw(5000)
obj1.CalculateInterest()