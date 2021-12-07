import random
h = []
k = 0
for i in range (1,11):
    h.append (random.randint(0,10))
print(h)
for i in range (len(h)):
    if h[i] == i:
        k = k + h[i]
print(k)