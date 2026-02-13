a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


maximum = lambda x, y: x if x > y else y

print("Maximum number is:", maximum(a, b))
