import threading

def Even():
    print("Even Numbers:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

def Odd():
    print("Odd Numbers:")
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=Even)
    thread2 = threading.Thread(target=Odd)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()