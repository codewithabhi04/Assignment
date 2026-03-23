import sys

source = sys.argv[1]

f1 = open(source, "r")

f2 = open("Demo.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("File copied successfully")