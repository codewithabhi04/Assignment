class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        count = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                count += 1
        return count == 2

    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i
        return sum

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value


obj = Numbers(17)

print("Prime:", obj.ChkPrime())
print("Factors:", end=" ")
obj.Factors()
print("Sum:", obj.SumFactors())
print("Perfect:", obj.ChkPerfect())