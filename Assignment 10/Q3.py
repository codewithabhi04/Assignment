# wpp which accept one number and print factorial of that number

No1 = int(input("Enter the num:"))

fact = 1
for i in range(1, No1 + 1):
    fact *= i

print(fact)
