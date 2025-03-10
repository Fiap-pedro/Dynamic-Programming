lista = [["banana", 1, 152], ["maça", 3, 100], ["uva", 1, 135], ["laranja", 2, 234]]

lista_ordenada = sorted(lista, key=lambda z: (z[1], z[0]))

print(lista_ordenada)
