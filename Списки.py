import random
# n = int(input())
# a = [i for i in range(1,n+1)]
# print(a)
# b = [i*2 for i in range(1,9)]
# print(b)
# c = [i for i in range(19,-1,-1)]
# print(c)
# f = []
# for i in range (1,11):
# f.append (random.randint(100,999))
# print(f)
# x = [i for i in ("python")]
# print(x)
# v = str(input())
# s = [i for i in (v)]
# print(v)
h = []
l = 0
sum = 0
k = 0
for i in range (1,21):
    h.append (random.randint(-10,10))
print(h)
for i in range (len(h)):
    sum = k + h[i]
    if h[i] >= 0:
        l = l + 1
    if h[i] < 0 :
        k = k + h[i]
print(sum)
print(l)
print(k)
#    h.append (random.randint(-10,10))
#print(h)
#for i in range (len(h)):
 #   print(h[i])
#k = h[0]
 #   l = h[1]
#    sum = k+l
#    print(sum)
#    print(h[1])
#    h = []