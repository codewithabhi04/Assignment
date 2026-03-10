import threading

def Maximum(lst):
    print("Maximum element:", max(lst))

def Minimum(lst):
    print("Minimum element:", min(lst))

numbers = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=Maximum, args=(numbers,), name="Thread1")
t2 = threading.Thread(target=Minimum, args=(numbers,), name="Thread2")

t1.start()
t1.join()

t2.start()
t2.join()