m, n,  = map(int, input().split())
k = 1
while (m % n >0 and n % m >0):
    k = k + 1
    if m > n :
        m = m % n
    else:
        n = n % m
print(min(m,n), k)