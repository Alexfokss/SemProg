import math
import random
import time

m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)











# Сортировка Шелла
# print("")          print("Сортировка Шелла")

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

# start = time.time()
# shell(m)
# print("-— %s seconds —-" % (time.time() - start))
# print(m)

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

# start = time.time()
# poosurek(m)
# print("-— %s seconds —-" % (time.time() - start))

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

# start = time.time()
# vstavki(m)
# print("-— %s seconds —-" % (time.time() - start))

##############################################################

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

# start = time.time()
# vubor(m)
# print("-— %s seconds —-" % (time.time() - start))

##############################################################

print()
print("Сортировка Шелла")
print(m)
start = time.time()
shell(m)
print("-— %s seconds —-" % (time.time() - start))
print(m)
print()

##############################################################

print()
print("Сортировка Пузырьком")
print(m)
start = time.time()
poosurek(m)
print("-— %s seconds —-" % (time.time() - start))
print()

##############################################################

print()
print("Сортировка Вставками")
print(m)
start = time.time()
vstavki(m)
print("-— %s seconds —-" % (time.time() - start))
print()

##############################################################

print()
print("Сортировка Выбором")
print(m)
start = time.time()
vubor(m)
print("-— %s seconds —-" % (time.time() - start))
print()

##############################################################