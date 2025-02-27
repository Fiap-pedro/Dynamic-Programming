lista = [10, 15, 20, 25, 30]


def indice_do_alvo(lista, alvo):
    i = 0
    while lista[i] != alvo:
        i += 1
        if lista[i] == alvo:
            return i
        break


print(indice_do_alvo(lista, 10))
