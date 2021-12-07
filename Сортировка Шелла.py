import math
import random
import time

m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)













# Сортировка Шелла

##############################################################
def shell(m):
    inc = len(m) // 2
    _count = 1
    while inc:
        for i, el in enumerate(m):
            while i >= inc and m[i - inc] > el:
                _count = _count + 1
                m[i] = m[i - inc]
                i -= inc
            m[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    print("Колличество итераций = ", _count)   
    return m
##############################################################

start = time.time()
shell(m)
print("-— %s seconds —-" % (time.time() - start))
print(m)

##############################################################







