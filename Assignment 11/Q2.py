#wpp which accepts one number and prints count of digits in that number 

num = int(input("Enter the number: "))

count = 0

while num != 0:
    count = count + 1
    num = num // 10

print("Count of digits is:", count)
