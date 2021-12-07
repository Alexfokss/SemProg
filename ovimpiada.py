# poryadkov_nomer -- порядковый номер участника
# pervay_b -- первая буква фамилии номер участника
# dlina -- длина имени участника
# kol_balov -- количество баллов
# unikal_nomer -- уникальный номер каждого участника
# b -- имя участника
# uchastnik_s_n_b -- имя участника, который в сумме по 
# трём олимпиадам набрал наибольше количество баллов
# vse_ucheniki -- количество учеников, принявших участие во всех трех олимпиадах
Olimpiada = dict()
ucheniki_ball = dict()
# def much_ballov():
# 
vse_ucheniki = 0
def f1():
    ol_1 = dict()
    global vse_ucheniki
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 1 олипиады ")
    h1 = int(input())
    for i in range(h1):
        poryadkov_nomer += 1
        print("Введите участника 1 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}"
        print("Уникальный номер", b,": ", f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        ol_1[unikal_nomer] = b
        ucheniki_ball[i+h2+h3] = f"{poryadkov_nomer}_{kol_balov}_{b}"
    vse_ucheniki = vse_ucheniki + h1
    Olimpiada[1] = ol_1
    print()
    print()
    print(Olimpiada)
    print()
    print()

def f2():
    ol_2 = dict()
    global vse_ucheniki
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 2 олипиады ")
    h2 = int(input())
    for i in range(h2):
        poryadkov_nomer += 1
        print("Введите участника 2 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}"
        print("Уникальный номер", b,": ", f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        ol_2[unikal_nomer] = b
        ucheniki_ball[i+h2+h3] = f"{poryadkov_nomer}_{kol_balov}_{b}"
    vse_ucheniki = vse_ucheniki + h2
    Olimpiada[2] = ol_2
    print()
    print()
    print(Olimpiada)
    print()
    print()


def f3():
    ol_3 = dict()
    global vse_ucheniki
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 3 олипиады ")
    h3 = int(input())
    for i in range(h3):
        poryadkov_nomer += 1
        print("Введите участника 3 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}"
        print("Уникальный номер", b,": " , f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        ol_3[unikal_nomer] = b
        ucheniki_ball[i+h2+h3] = f"{poryadkov_nomer}_{kol_balov}_{b}"
    vse_ucheniki = vse_ucheniki + h3
    Olimpiada[3] = ol_3
    print()
    print()
    print(Olimpiada)
    print()
    print()

f1()
f2()
f3() 
print("Всего учеников, принявших участие во всех трех олимпиадах = ", vse_ucheniki)



#  Лисов Денис    Вера Жукова   Артём Полков       Сергей Чашкин    Маша Ролева    Полина Крылова   

