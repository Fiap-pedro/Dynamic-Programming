from time import sleep


def busca_binaria(lista, alvo):
    # Ordenando a lista
    lista_ordenada = sorted(lista)
    # "l" representa o índice 0 da lista, o ínicio
    l = 0
    # "h" representa o último índice da lista
    h = len(lista_ordenada) - 1

    for iteracao in range(len(lista_ordenada)):
        # Fórmula para encontrar o meio da lista
        m = (l + h) // 2
        print(f"{iteracao}: m={m}, l={l}, h={h}")
        sleep(0.5)
        # Após encontrar o meio da lista:

        #Se o valor intermediário for igual ao alvo:
        if lista[m] == alvo:
            return m

        # Se o valor intermediário for menor que o alvo:
        elif lista[m] < alvo:
            l = m + 1

        # Se o valor intermediário for maior que o alvo:
        else:
            h = m - 1
    # Se der algum erro vai retornar -1
    return -1
