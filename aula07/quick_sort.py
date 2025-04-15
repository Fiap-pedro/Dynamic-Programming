lista = [10, 80, 30, 24, 4, 8, 16]


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    maiores = [x for x in lista[:-1] if x >= pivo]
    menores = [x for x in lista[:-1] if x <= pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


print(quick_sort(lista))
