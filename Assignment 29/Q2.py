filename = input("Enter file name: ")

File = open(filename, "r")

data = File.read()

print(data)

File.close()