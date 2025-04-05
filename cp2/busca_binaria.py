from time import sleep


def busca_binaria(lista, alvo):
    lista_ordenada = sorted(lista)
    l = 0
    h = len(lista_ordenada) - 1

    for iteracao in range(len(lista_ordenada)):
        m = (l + h) // 2
        print(f"{iteracao}: m={m}, l={l}, h={h}")
        sleep(0.5)
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return -1
