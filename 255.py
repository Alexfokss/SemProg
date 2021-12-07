#№255
# a координаты строки слона
# b координаты столбца слона
# c координаты строки фигуры
# d координаты столбца фигуры
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a-c==1:
    print("YES")
elif c-a==1:
    print("YES")
elif b-d==1:
    print("YES")
elif d-b==1:
    print("YES") 
else:
    print("NO")


# a координаты строки ладьи
# b координаты столбца ладьи
# c координаты строки фигуры
# d координаты столбца фигуры
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c:
    print("YES")
elif b==d:
    print("YES")
else:
    print("NO")


