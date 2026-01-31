# wpp which accept one number and print sum of the first N natural number
 

No1 = int(input("Enter the num:"))

sum = 0
for i in range(1, No1 + 1):
    sum = sum + i

print(sum)
