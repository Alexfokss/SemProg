import random
a = []
for g in range(0,11):
    a.append(random.randint(0,10))
print(a)
def q():
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            while a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
# while  
# q()
# print(a)