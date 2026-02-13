a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
d = int(input("Enter third number:"))


largest = lambda x, y, z: x if (x > y and x > z) else (y if y > z else z)
print("largest num is:", largest(a,b,d))
