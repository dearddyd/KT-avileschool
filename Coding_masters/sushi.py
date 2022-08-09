a = str(input("입력: "))

a1 = []
b1 = [1000, 1500, 2000, 3000, 5000]
a1 = a.split()
a1_int = list(map(int, a1))

#print(a1_int)
#print(b1)

Sum_ = 0
for i in range(0,len(a1_int)):
    Sum_ += a1_int[i] * b1[i]
    print(Sum_)
print(Sum_)