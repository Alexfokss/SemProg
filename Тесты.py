import time
def bin_search(a,x):
    b = False
    left = 0
    right = len(list_1)- 1
    while left <= right:
        mid = (right + left) // 2
        if x > a[mid]:
            left = mid+1
        elif x < a[mid]:
            right = mid-1
        else:
            b = True
            break
    if b:
        return 'Yes'
    else:
        return 'No'
def search(a,x):
    for i in range(0,len(a)):
        if a[i] == x:
            return "YES"
    return "NO"




list_1 = [i for i in range(1,1000000000000)]
x = 4
start = time.time()
print (bin_search (list_1, x))
print("-— %s seconds —-" % (time.time() - start))
start = time.time()
print(search(list_1, x))
print("-— %s seconds —-" % (time.time() - start))
