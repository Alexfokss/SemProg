m, n = map(int, input().split())
k = 1
if m<n:
    c = n
    d = m
    m = c
    n = d
while (n < m and n!=0 and m!=0):
    k = k + 1
    if m > n :
        m = m-n 
    elif n < m:
        n = n - m      
print(min(m,n), k)