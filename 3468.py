n = int(input())
a = n//60
b = n%60
if a == 24:
    print(0,b)
elif a > 24:
    print(0,b)
else:
    print(a,b)
