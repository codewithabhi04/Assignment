#wpp which accepts one number and prints reverse that number 

num = int(input("Enter the number: "))


while num != 0:
    rev = num % 10
    num = int(num / 10)
    print(rev,end=" ")




