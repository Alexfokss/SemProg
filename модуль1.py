a = int(input())
b = a//1000
c = a%10
d = (a//100)%10
e = (a%100)//10
if (b == c) and (d == e):
    print(1)
elif (b == c) or (d == e):
    print(1)
else:
    print(0)
