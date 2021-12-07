a, b, = map(int,input().split())
k = 1
while a!=b:
    k = k + 1
    if a > b :
        a = a - b
    else:
        b = b - a 
print(min(a,b),k)