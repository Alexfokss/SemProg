# d - длина норы
# z - здоровье
# v - вес
# u - уважение
d = 10
z = 100
u = 20
v = 30     
import math
import random
def night():
    # ночь
    if  ((a == 5) or (a == 6) or (a == 7 or (a == 8)):
        d= d -2
        z =z +20
        u = u - 2
        v = v - 5
        check()
        status()
#########################
def status():
    print("Длина норы ="d)
    print("Здоровье ="z)
    print("Вес ="v)
    print("Уважение ="u)
#############################
def day():
    if a == 8
        night()
        night()
        night()
        check()
        status()
############################
def check():
    if u >= 100
        print("VICTORY!")
        
    if ( d == 0 or z == 0 or u == 0 v == 0):
        print("GAME OVER")
########################################
def dig():
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
    status()
##########################################################
def eat():
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
    status()
#######################################################
def fight():
    if a == 7:
        print("Введите 1, чтобы пойти подраться со слабым существом (v = 30)")
        print("Введите 2, чтобы пойти подраться со средним существом (v = 50)")
        print("Введите 3, чтобы пойти подраться с сильным существом (v = 70)")
        a1 = int(input())
        
        # СЛАБОЕ

        if a1 == 1:
        g = v/v+30
        s = s.round(g,1)
        vr_victory = s%10
        b = random.randint(1,9)
        if vr_victory < b:
            print("Поражение")
            z = z -35
            v - 15
        if vr_victory == b:
            print("Победа")
            u1 = u1 + 10
            z1 = z1-10
        else:
            print("Победа")
            u1 = u1+15
            z1 = z1-15
        
        # СРЕДНЕЕ

        if a1 == 2:
        g = v/v+50
        s = s.round(g,1)
        vr_victory = s%10
        b = random.randint(1,9)
        if vr_victory < b:
            print("Поражение")
            z = z -55
            v - 35
        if vr_victory == b:
            print("Победа")
            u1 = u1 + 30
            z1 = z1-30
        else:
            print("Победа")
            u1 = u1+25
            z1 = z1-25
        # СИЛЬНОЕ

        if a1 == 3:
        g = v/v+70
        s = s.round(g,1)
        vr_victory = s%10
        b = random.randint(1,9)
        if vr_victory < b:
            print("Поражение")
            z = z -75
            v - 55
        if vr_victory == b:
            print("Победа")
            u1 = u1 + 45
            z1 = z1-45
        else:
            print("Победа")
            u1 = u1+40
            z1 = z1-40
        check()
        status()
#########################################################
def consol():
    print("Введите 5, чтобы копать нору")
    print("Введите 6, чтобы поесть травку")
    print("Введите 7, чтобы пойти подраться")
    print("Введите 8, чтобы поспать весь день")
    a = int(input())
####################################################  
d = 10
z = 100
u = 20
v = 30           
While ( u >= 100 and d !=0 and z!=0 and v !=0):
    consol()
    dig()
    eat()
    fight()
    day()

