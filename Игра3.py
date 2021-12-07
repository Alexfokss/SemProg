# d - длина норы
# z - здоровье
# v - вес
# u - уважение
# g - простоя переменная
# s - простоя переменная
d = 10
z = 100
u = 20
v = 30
g = 0  
s = 0 
import math
import random
def night():
    # ночь
    global d
    global z
    global v
    global u
    d = d - 2
    z = z + 20
    u = u - 2
    v = v - 5
    check()
    status()
    consol()
####################################################
def status():
    print("Длина норы =",d)
    print("Здоровье =",z)
    print("Вес =",v)
    print("Уважение =",u)
####################################################
def day():
    if a == 8:
        global d
        global z
        global v
        global u
        d = d - 6
        z = z + 60
        u = u - 6
        v = v - 15
        check()
        status()
####################################################
def check():
    global d
    global z
    global v
    global u
    if ((u >= 100) and (u != 0) and (d != 0) and (z != 0) and (v != 0)):
        print("VICTORY!")  
    if ((d <= 0) or (z <= 0) or (u <= 0) or (v <= 0)):
        print("GAME OVER")
####################################################
def dig():
    global u
    global v
    global d
    global z
    if a == 5:
        print("Введите 1, чтобы интенсивно копать нору")
        print("Введите 2, чтобы лениво копать нору")
    a1 = int(input())
    # интенсивно
    if a1 == 1 :
        d = d + 5
        z = z - 30
    # лениво
    if a1 == 2 :
        d = d + 2 
        z = z - 10
    check()
    night()
####################################################
def eat():
    global d
    global z
    global v
    global u
    if a == 6:
        print("Введите 1, чтобы поесть зелёную травку")
        print("Введите 2, чтобы поесть жухлую травку")   
    a1 = int(input())
    # жухлой
    if a1 == 1:
        z = z + 10
        v = v + 15
    # зёленой
    if a1 == 2 :
        if u < 30:
            z = z - 30
        if u >= 30:
            z = z + 30
            v = v + 30
        else:
            print("Существо не может посетит площадку из-за недостатка уважения")
    check()
    night()
####################################################
def fight():
    global d
    global z
    global v
    global u
    if a == 7:
        print("Введите 1, чтобы пойти подраться со слабым существом (v = 30)")
        print("Введите 2, чтобы пойти подраться со средним существом (v = 50)")
        print("Введите 3, чтобы пойти подраться с сильным существом (v = 70)")
        a1 = int(input())
        
        # СЛАБОЕ

        if a1 == 1:
            g = v / (v + 30)
            s = round(g,1)
            vr_victory = s % 10
            b = random.randint(1,9)
            if vr_victory < b:
                print("Поражение")
                z = z - 35
                v = v - 15
            if vr_victory == b:
                print("Победа")
                u = u + 10
                z = z - 10
            if vr_victory > b:
                print("Победа")
                u = u + 15
                z = z - 15
        
            # СРЕДНЕЕ

        if a1 == 2:
            g = v / (v+50)
            s =round(g,1)
            vr_victory = s % 10
            b = random.randint(1,9)
            if vr_victory < b:
                print("Поражение")
                z = z - 55
                v = v - 35
            if vr_victory == b:
                print("Победа")
                u = u + 30
                z = z - 30
            if vr_victory > b:
                print("Победа")
                u = u + 25
                z = z - 25
            # СИЛЬНОЕ

        if a1 == 3:
            g = v / (v + 70)
            s = round(g,1)
            vr_victory = s % 10
            b = random.randint(1,9)
            if vr_victory < b:
                print("Поражение")
                z = z - 75
                v = v - 55
            if vr_victory == b:
                print("Победа")
                u = u + 45
                z = z - 45
            if vr_victory > b:
                print("Победа")
                u = u + 40
                z = z - 40
        check()
        night()
####################################################
def consol():
    print("Введите 5, чтобы копать нору")
    print("Введите 6, чтобы поесть травку")
    print("Введите 7, чтобы пойти подраться")
    print("Введите 8, чтобы поспать весь день")
####################################################
def game():
    if a == 5:
        dig()
    if a == 6:
        eat()
    if a == 7:
        fight()
    if a == 8:
        day()
####################################################  
d = 10
z = 100
u = 20
v = 30   
consol()        
while u < 100 and u > 0 and d > 0 and z > 0 and v > 0:
    a = int(input())
    game()
    