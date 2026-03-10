
num = int(input("Number of elements: "))

store = []

for i in range(num):
    Ele = int(input("Element: "))
    store.append(Ele)

def Add(store):
    total = 0
    for i in store:
        total += i
    return total

print(store)   
Add(store)




