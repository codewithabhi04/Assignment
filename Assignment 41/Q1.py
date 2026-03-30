import math

data = [
    ('A', 1, 2, 'Red'),
    ('B', 2, 3, 'Red'),
    ('C', 3, 1, 'Blue'),
    ('D', 6, 5, 'Blue')
]
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

distances = []
for point in data:
    name, x1, y1, label = point
    dist = math.sqrt((x - x1)**2 + (y - y1)**2)
    distances.append((name, dist, label))

distances.sort(key=lambda d: d[1])


k = 3   #top 3 nearest points.
neighbors = distances[:k]

print("\nNearest Neighbors:")
for n in neighbors:
    print(f"{n[0]} - Distance: {round(n[1], 2)}")

count = {}
for n in neighbors:
    label = n[2]
    count[label] = count.get(label, 0) + 1

predicted_class = max(count, key=count.get)

print("\nPredicted Class:", predicted_class)