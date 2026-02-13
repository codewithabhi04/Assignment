L = [2,3,4,5,6,7,8,9,10,15]

LIST1 = list(filter(lambda x: x%3==0 and x%5==0, L))

print(LIST1)