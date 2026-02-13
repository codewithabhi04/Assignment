from functools import reduce
L = [2,3,4,5,6,7,8,9,10]

LIST1 = reduce(lambda x,y: x*y, L)

print(LIST1)




