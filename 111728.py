import random
def q():
    if a[j] > a[j+1]:
        a[j],a[j+1] = a[j+1],a[j]
        print(a)
    return
j = 0
с = 0
n, m = map(int, input().split())
a = [0]*n
for i in range(len(a)):
    a[i] = random.randint(1,100)
print(a)
for j in range(0,len(a)-1):
    q()
    if a[j] > a[j+1]:
        a[j],a[j+1] = a[j+1],a[j]
        print(a)
    if a[j] < a[j-1] and j != 0:
        a[j],a[j-1] = a[j-1],a[j]
        print(a)

b = [0]*m
for i in range(len(b)):
    b[i] = random.randint(1,20000)
print(a)
print(b)
# r = 0
# f = 1
# b = []
# for i in range(0,k):
#     b.append(random.randint(k,101))