class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    def Addition(self):
        print("Addition =", self.Value1 + self.Value2)

    def Subtraction(self):
        print("Subtraction =", self.Value1 - self.Value2)

    def Multiplication(self):
        print("Multiplication =", self.Value1 * self.Value2)

    def Division(self):
    
        print("Division =", self.Value1 / self.Value2)


obj1 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()