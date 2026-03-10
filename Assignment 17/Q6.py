

num = int(input("Enter the number: "))

for a in range(num,0,-1):
    for b in range(a):
        print("*", end=" ")
    print()
