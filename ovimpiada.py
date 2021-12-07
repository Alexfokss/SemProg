# poryadkov_nomer -- порядковый номер участника
# pervay_b -- первая буква фамилии номер участника
# dlina -- длина имени участника
# kol_balov -- количество баллов
# unikal_nomer -- уникальный номер каждого участника
# b -- имя участника
# uchastnik_s_n_b -- имя участника, который в сумме по
# трем олимпиадам набрал наибольше количество баллов. 	
# kol_uchenik -- количество участников									
Olimpiada = dict()

# def much_ballov():
#     uchastnik_s_n_b = b
#     kol_balov = p
#     if > :
#         sum_balov

def f1():
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 1 олипиады ")
    h = int(input())
    for i in range(h):
        poryadkov_nomer += 1
        print("Введите участника 1 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
        print("Уникальный номер", b,": ", f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        Olimpiada[unikal_nomer] = b
    print()
    print()
    print(Olimpiada)
    print()
    print()

def f2():
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 2 олипиады ")
    h = int(input())
    for i in range(h):
        poryadkov_nomer += 1
        print("Введите участника 2 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
        print("Уникальный номер", b,": ", f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        Olimpiada[unikal_nomer] = b
    print()
    print()
    print(Olimpiada)
    print()
    print()


def f3():
    poryadkov_nomer = 0
    b = ""
    print("Введите количество участников 3 олипиады ")
    h = int(input())
    for i in range(h):
        poryadkov_nomer += 1
        print("Введите участника 3 олипиады ")
        print("Введите количество набранных баллов ")
        b = str(input())
        kol_balov = int(input())
        pervay_b = b[0]
        dlina = len(b)
        print()
        unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
        print("Уникальный номер", b,": " , f"{poryadkov_nomer}_{pervay_b[0]}_{dlina}")
        print()
        Olimpiada[unikal_nomer] = b
    print()
    print()
    print(Olimpiada)
    print()
    print()

f1()
f2()
f3()




#{'1_Л_34': 'Лисов Денис', '2_В_56': 'Вера Жукова', '1_А_87': 'Артём Полков', '2_С_34': 'Сергей Чашкин', '1_М_45': 'Маша Ролева', '2_П_29': 'Полина Крылова'} 