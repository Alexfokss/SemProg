import math
import random
import time


m = []
for i in range(10):
    m.append(random.randint(1, 11))
print(m)

##############################################################

def partition(m, begin, end):
    pivot = begin
    for i in range (begin + 1, end + 1):
        if m[i] <= m[begin]:
            pivot += 1
            m[i], m[pivot] = m[pivot], m[i]
    m[pivot], m[begin] = m[begin], m[pivot]
    return pivot

def quick_sort(m, begin = 0, end = None):
    if end is None:
        end = len(m) - 1
    
    def _quicksort(m, begin, end):
        if begin >= end:
            return
        pivot = partition(m, begin, end)
        _quicksort(m, begin, pivot-1)
        _quicksort(m, pivot + 1, end)
    return _quicksort(m, begin, end)



##############################################################

# start = time.time()
# bin_search(m, x)
# print("-— %s seconds —-" % (time.time() - start))

##############################################################

quick_sort(m, begin = 0, end = None)
