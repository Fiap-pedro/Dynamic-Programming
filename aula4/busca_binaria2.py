from bubble_sort import bubble_sort


def busca_binaria(lista, alvo):
    lista_ordenada = bubble_sort(lista)
    l = 0
    h = len(lista_ordenada) - 1

    for iteracao in range(len(lista_ordenada)):
        m = (l + h) // 2
        print(f"{iteracao}: m={m}, l={l}, h={h}")

        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return -1


print(busca_binaria([11, 17, 18, 45, 50, 67], 18))
