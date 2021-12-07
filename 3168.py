from _typeshed import _KT_contra


a = list(map(int,input().split()))
for i in range(0,len(a)-1):
    if a[i] == 0:
        a.append(0)
print(a)