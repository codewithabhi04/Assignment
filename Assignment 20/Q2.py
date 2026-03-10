import threading

def EvenFactor(n):
    even = 0
    print("Even factors:")
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            print(i, end=" ")
            even += i
    print("\nSum of even factors:", even)

def OddFactor(n):
    odd = 0
    print("Odd factors:")
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            print(i, end=" ")
            odd += i
    print("\nSum of odd factors:", odd)

num = int(input("Enter a number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))

t1.start()
t1.join()   

t2.start()
t2.join()   

print("Exit from main")