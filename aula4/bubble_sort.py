lista = [23, 12, 6, 34, 12, 9, 10, 1, 5]

for i in range(len(lista)):
    maior = lista[0]
    menor = 0
    if lista[i] < maior:
        menor = lista[i]
        lista[i] = menor
        lista[i+1] = maior
    print(lista)
