import threading

def Prime(lst):
    print("Prime numbers:")
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print()


def NonPrime(lst):
    print("Non-prime numbers:")
    for num in lst:
        if num <= 1:
            print(num, end=" ")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print(num, end=" ")
                    break
    print()


numbers = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Prime, args=(numbers,), name="Prime")
t2 = threading.Thread(target=NonPrime, args=(numbers,), name="NonPrime")

t1.start()
t1.join()

t2.start()
t2.join()