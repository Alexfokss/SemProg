a = list(map(int,input().split()))
for i in range(len(a)-1,0,-1):
    a[i], a[i-1] = a[i-1], a[i]
#  a[0], a[len(a)-1] = a[len(a)-1], a[0]
print(*a)






# a = list(map(int,input().split()))
# b = 0
# c = 0
# d = []
# d.append(len(a))
# for i in range(len(a)):
# b = a[i]
# d.append(b)
# c = len(d)
# del d[-1]
# print(d)