import random

print('Быстрая сортировка')

m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)

def quicksort(m):
    fst, lst = 0, 0
    if fst >= lst: return

    i, j = fst, lst
    pivot = m[random.randint(fst, lst)]

    while i <= j:
        while m[i] < pivot: i += 1
        while m[j] > pivot: j -= 1
        if i <= j:
            m[i], m[j] = m[j], m[i]
            i, j = i + 1, j - 1
            
    quicksort(m, fst, j)
    quicksort(m, i, lst)

quicksort(m)

print(m)