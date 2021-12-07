a = list(map(int,input().split()))
def zero():
    if a[i] == 0:
        del a[i]
        a.remove(a[i])
for i in range(0,len(a)-1):
    zero()
    if a[i] == 0:
        del a[i]
        a.append(0)
    if a[i-1] == 0:
        del a[i-1]
        a.append(0)
    if a[i+1] == 0:
        del a[i+1]
        a.append(0)
if a[i] == 0:
        del a[i]
        a.append(0)
if a[i+1] == 0:
        del a[i+1]
        a.append(0)      
print(a)