import random
n = int(input())
a = []
for i in range (n):
    a.append (random.randint(1,11))
print(a)
p = len(a)//2
for i in range(p,len(a)-1):
    while a[i]<= a[p]:
        i = i + 1
    if a[i] >= a[j]:
        a[i],a[j] = a[j],a[i]
    for j in range(p,1,-1):
        while a[i] >= a[p]:
            j = j - 1 
        if a[i] <= a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
# def Rec(a):
#     if a > 1 :
#         return Rec (a - 1)
#     else:
#         return 5
# print(Rec(3))