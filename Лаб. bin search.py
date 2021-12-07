import time
import math
import random
m = [l for l in range(1,11)]
n = [l for l in range(1,101)]
o = [l for l in range(1,1001)]
_count = 1
for i in range(11):
    m.append(random.randint(1, 11))
print(m)
 

k = 0
start = 0

# Пузырёк


def poosurek():
    for i in range(len(m)-1):
        for j in range(m-i-1):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
            _count = _count + 1
    print(m)
    print("_count = ", _count)
    start = time.time()
    print (poosurek(m))
    print("-— %s seconds —-" % (time.time() - start))


# Вставками


def vstavki(m):
    for i in range(1, len(m)):
        temp = m[i]
        j = i - 1
        while (j >= 0 and temp < m[j]):
            m[j + 1] = m[j]
            j = j - 1
        _count = _count + 1
        m[j + 1] = temp
    print(m) 
    print("_count = ", _count)
    start = time.time()
    print(vstavki(m))
    print("-— %s seconds —-" % (time.time() - start))

# Выбором


def vubor(m):
    for i in range(len(m) - 1):
        k = i
        j = i + 1
        while j < len(m):
            if m[j] < k[m]:
                k = j
            _count = _count + 1
            j = j + 1
        m[i], m[m] = m[m], m[i]
    print(m)
    print("_count = ", _count)
    start = time.time()
    print(vubor(m))
    print("-— %s seconds —-" % (time.time() - start))

# шелла




def shell(m):
    inc = len(m) // 2
    while inc:
        for i, el in enumerate(m):
            while i >= inc and m[i - inc] > el:
                m[i] = m[i - inc]
                i -= inc
            m[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return m


# Быстрая сортировка


def bin_search(m,x):
    b = False
    left = 0
    right = len(m)- 1
        while left <= right:
            mid = (right + left) // 2
            _count = _count + 1
        if x > m[mid]:
                left = mid+1
        elif x < m[mid]:
                right = mid-1
        else:
                b = True
                break
        if b:
            return 'Yes'
        else:
            return 'No'
    print(m)
    print("_count = ", _count)
    start = time.time()
    print(bin_search(m, x))
    print("-— %s seconds —-" % (time.time() - start))








