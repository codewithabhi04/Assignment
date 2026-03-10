
num = int(input("Number of elements: "))

store = []

for i in range(num):
    Ele = int(input("Element: "))
    store.append(Ele)

min_val = store[0]
for x in store:
    if x < min_val:
        min_val = x


print(store) 
print("Minimum:", min_val)

