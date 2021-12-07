import math
import random
import time


m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)
##############################################################

def poosurek(m):
    _count = 1
    for i in range(len(m)-1):
        for j in range(len(m)-i-1):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
                _count = _count + 1
    print(m)
    print("Колличество итераций = ", _count)

##############################################################

start = time.time()
poosurek(m)
print("-— %s seconds —-" % (time.time() - start))
