#wpp which accepts oone number and check whether it is prime or not 

n=int(input("Enter a number"))

if n<=1:
   print("not prime")
else:
   for i in range(2,n):
        if n%2==0 :
            print("Not Prime")
            break
        else:
            print("Prime")
            break