from time import sleep


def entrada_carros():
    lista = []
    for i in range(10):
        lista.append(input("Digite o modelo do carro: "))
    return lista


def lifo(lista):
    for i in range(len(lista)):
        saindo = lista.pop(-1)
        print(f"{i+1}º a sair: {saindo}")
        sleep(0.5)
    print("Acabou.")

