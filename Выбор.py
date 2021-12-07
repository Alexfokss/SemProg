import math
import random
import time


m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)

##############################################################

def vubor(m):
    _count = 1
    for i in range(len(m) - 1):
        k = i
        j = i + 1
        while j < len(m):
            if m[j] < m[k]:
                k = j
            _count = _count + 1
            j = j + 1
        m[i], m[k] = m[k], m[i]
    print(m)
    print("Колличество итераций = ", _count)

##############################################################

start = time.time()
vubor(m)
print("-— %s seconds —-" % (time.time() - start))

##############################################################
