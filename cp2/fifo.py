from time import sleep


def entrada_clientes():
    lista = []
    for i in range(10):
        lista.append(input("Digite o nome do cliente: "))
    return lista


def fifo(lista):
    for i in range(len(lista)):
        saindo = lista.pop(0)
        print(f"{i+1}º a sair: {saindo}")
        sleep(0.5)
    print("Acabou.")


print(fifo(entrada_clientes()))
