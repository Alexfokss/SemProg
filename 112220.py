m, n,  = map(int, input().split())
k = 1
while n!=0:
    k = k + 1
    if m > n :
        m = m-n       
print(min(m,n), k)