

def Arithmetic():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    def Add(num1,num2):
        return num1 + num2
       

    
    def Sub(num1,num2):
        return num1 - num2

    def Mul(num1,num2):
        return num1 * num2

    def Div(num1,num2):
        return num1 / num2
    
    
    print("Addition:", Add(num1, num2))
    print("Subtraction:", Sub(num1, num2))
    print("Multiplication:", Mul(num1, num2))
    print("Division:", Div(num1, num2))

Arithmetic()
