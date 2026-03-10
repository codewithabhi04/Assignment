import threading

def EvenList(lst):
    n = 0
    for i in lst:
        if i % 2 == 0:
            print(i, end=" ")
            n += i
    print("\nSum of even:", n)

def OddList(lst):
    n = 0
    for i in lst:
        if i % 2 != 0:
            print(i, end=" ")
            n += i
    print("\nSum of odd:", n)

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=EvenList, args=(lst,))
t2 = threading.Thread(target=OddList, args=(lst,))

t1.start()
t1.join()   

t2.start()
t2.join()  