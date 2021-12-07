b = int(input())
k = 0
c = 0
d = 0
while b%10 == 0:
    k = k + 1
    c = k
    if b%10 != 0:
        d = k
        k = 0
    if c != d or d != c:
        c = d
        d = 0
    print(c)
    print(k)
print(c)
print(k)


