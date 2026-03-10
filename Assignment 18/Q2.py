
num = int(input("Number of elements: "))

store = []

for i in range(num):
    Ele = int(input("Element: "))
    store.append(Ele)

max_val = 0
for x in store:
    if x > max_val:
        max_val = x


print(store) 
print("Maximum:", max_val)


  






