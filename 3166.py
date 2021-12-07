a = list(map(int,input().split()))
b = 0
c = 0
for i in range(len(a)-1):
    b = a[i+1]
    a[i] = a[i+1]

    print(a)

# a = list(map(int,input().split()))
# b = 0
# c = 0
# d  = []
# d.append(len(a))
# for i in range(len(a)):
#     b = a[i]
#     d.append(b)
#     c = len(d)
# del d[-1]
# print(d)
