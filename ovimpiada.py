# poryadkov_nomer -- порядковый номер участника
# pervay_b -- первая буква фамилии номер участника
# dlina -- длина имени участника
# kol_balov -- количество баллов
# unikal_nomer -- уникальный номер каждого участника
# b -- имя участника

def olimpiada():
    Olimpiada = dict()

    def f1():
        poryadkov_nomer = 0
        b = ""
        print("Введите количество участников 1 олипиады ")
        h = int(input())
        for i in range(h):
            poryadkov_nomer += 1
            print("Введите участника 1 олипиады ")
            print("Введите количество набранных баллов ")
            a = {}
            b = str(input())
            pervay_b = b
            kol_balov = int(input)
            a.add(b)
            dlina = len(b)
            print(a)
            print()
            unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
            print("Уникальный номер", b, f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}")
            a[unikal_nomer] = b
            Olimpiada['1'] = a

    def f2():
        poryadkov_nomer = 0
        b = ""
        print("Введите количество участников 2 олипиады ")
        h = int(input())
        for i in range(h):
            poryadkov_nomer += 1
            print("Введите участника 2 олипиады ")
            print("Введите количество набранных баллов ")
            c = {}
            b = str(input())
            pervay_b = b
            kol_balov = int(input)
            c.add(b)
            dlina = len(b)
            print(c)
            print()
            unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
            print("Уникальный номер", b, f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}")
            c[unikal_nomer] = b
            Olimpiada['2'] = c


    def f3():
        poryadkov_nomer = 0
        b = ""
        print("Введите количество участников 3 олипиады ")
        h = int(input())
        for i in range(h):
            poryadkov_nomer += 1
            print("Введите участника 3 олипиады ")
            print("Введите количество набранных баллов ")
            d = {}
            b = str(input())
            pervay_b = b
            kol_balov = int(input)
            d.add(b)
            dlina = len(b)
            print(d)
            print()
            unikal_nomer = f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}"
            print("Уникальный номер", b, f"{poryadkov_nomer}_{pervay_b[0]}_{kol_balov}")
            d[unikal_nomer] = b
            Olimpiada['3'] = d

olimpiada()