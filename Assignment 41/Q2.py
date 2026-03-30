X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

mx = sum(X)/n
my = sum(Y)/n

m = sum((X[i]-mx)*(Y[i]-my) for i in range(n)) / sum((X[i]-mx)**2 for i in range(n))
c = my - m*mx

print("m =", round(m,2))
print("c =", round(c,2))
print("Y =", round(m,2),"X +", round(c,2))