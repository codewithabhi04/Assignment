##wpp which accepts one number and check  wheather it is plindrome or not


num = int(input("Enter the number: "))


while num != 0:
    rem = num % 10
    num = int(num / 10)
    print(rem,end=" ")

if num == rem:
    print("Plindrome")

else:
    print("Not plindrome")