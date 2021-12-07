import math
import random
import time


def shell(m):
    inc = len(m) // 2
    k = 1
    while inc:
        for i, el in enumerate(m):
            while i >= inc and m[i - inc] > el:
                k = k + 1
                m[i] = m[i - inc]
                i -= inc
            m[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    print("Колличество итераций = ", k)   
    return m
#

m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)
 

start = time.time()
shell(m)
print("-— %s seconds —-" % (time.time() - start))
print(m)

#shell(m)



