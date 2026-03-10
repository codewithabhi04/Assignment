
num = int(input("Number of elements: "))

store = []

for i in range(num):
    Ele = int(input("Element: "))
    store.append(Ele)

search = int(input("Element to search: "))

print(store) 

if search in store:
    print(store.count(search))




  






