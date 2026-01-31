# wpp which accept one number and prints its factors


Num = int(input("Enter any number:"))

for i in range(1,Num+1):
    if Num % i == 0:
        print(i)