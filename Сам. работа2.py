import random
n = int(input())
a = []
k = 0
b = 0
c = 0
d = 0
for i in range (n):
a.append (random.randint(1,11))
print(a)
for i in range (len(a)):
b = a[0]
c = a[1]
d = a[2]
if (c > b) and (c > d):
k = k + 1
del a[0]
print(k)