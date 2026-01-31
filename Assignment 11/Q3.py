#wpp which accepts one number and prints sum of digits in that number 

num = int(input("Enter the number: "))

sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = int(num / 10)

print("Sum of the digits:", sum)
