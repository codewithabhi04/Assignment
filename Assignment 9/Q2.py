# 2. wpp which contain one function named as ChkGreater() the accept two number and print geater number

def ChkGreater():
    No1 = int(input("Enter the first num:"))
    No2 = int(input("Enter the second num:"))

    if No1 >= No2:
        print(No1,"is Greater Number")
    else:
        print(No2,"is  Greater Number")

ChkGreater()
