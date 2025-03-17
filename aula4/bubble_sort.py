def bubble_sort(lista):
    x = 0
    for vezes in range(len(lista)-1, 0, -1):
        for i in range(vezes):
            if lista[i] > lista[i+1]:
                x = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = x
    return lista


print(bubble_sort([23, 12, 6, 34, 12, 9, 10, 1, 5]))
