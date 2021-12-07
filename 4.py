import random
n, k  = map(int,input().split())
a = [i for i in range(1,n+1)]
r = 0
f = 1
b = []
for i in range(0,k):
    b.append(random.randint(1,101))
print(a)
print(b)
for j in range(len(a)):
    print(r)
    while f>1:
        if a[j] == b[r]:
            print("YES")
        else:
            print("NO")
        r +=1
    if r == k:
        break
