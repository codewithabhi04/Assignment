from functools import reduce

user_input = input("Enter List items: ")

my_list = user_input.split()  

num_list = []
for item in my_list:
    num_list.append(int(item))

List1 = list(filter(lambda x: x >= 70  or x ==90, num_list))
List2 = list(map(lambda x: x+x, List1))
List3 = reduce(lambda x,y: x*y, List1)

print(List1)
print(List2)
print(List3)