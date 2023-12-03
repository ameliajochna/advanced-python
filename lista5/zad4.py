def usun_duplikaty(lista):
    lista_2 = []
    for i in range(len(lista)):
        lista_2 += [[lista[i], i]]

    lista_2.sort()
    lista_3 = []

    for i in range(len(lista_2)):
        if len(lista_3) == 0 or lista_3[-1:][0][1] != lista_2[i][0]:
            lista_3 += [[lista_2[i][1], lista_2[i][0]]]

    lista_3.sort()

    wynik = []

    for i in range(len(lista_3)):
        wynik += [lista_3[i][1]]

    return wynik


print(usun_duplikaty([1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]))
