import math
import random
import time


m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)

##############################################################

def vstavki(m):
    _count = 1
    for i in range(1, len(m)):
        temp = m[i]
        j = i - 1
        while (j >= 0 and temp < m[j]):
            m[j + 1] = m[j]
            j = j - 1
        _count = _count + 1
        m[j + 1] = temp
    print(m) 
    print("Колличество итераций = ", _count)

##############################################################

start = time.time()
vstavki(m)
print("-— %s seconds —-" % (time.time() - start))

##############################################################

