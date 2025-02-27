lista = [10, 20, 30, 40, 50]


def indice_do_alvo(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i


print(indice_do_alvo(lista, 30))
