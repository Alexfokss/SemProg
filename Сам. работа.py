n = int(input())
k = 0
b = n
c = 0
d = 0
g = 0
while b<10:
    g  +=1
    if b%10 == 0 and b//10 !=0:
        k = k + 1
        c = k
    if b%10 !=0:
        d = k
        k = 0
    if c < d or d > c:
        c = d
    b == b//10
print(c)
print(g)