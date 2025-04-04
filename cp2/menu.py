from busca_binaria import busca_binaria
from fifo import fifo, entrada_clientes
from lifo import lifo, entrada_carros

txtMenu = """
1 - busca binária
2 - lifo
3 - fifo
0 - sair
Escolha uma opção:
"""

while True:
    escolha = int(input(txtMenu))

    if escolha == 0:
        print("Saindo.")
        break

    elif escolha == 1:
        alvo = int(input("Escolha um alvo da lista [3, 5, 7, 8, 11, 14, 15]: "))
        busca_binaria([3, 5, 7, 8, 11, 14, 15], alvo)

    elif escolha == 2:
        lifo(entrada_carros())

    elif escolha == 3:
        fifo(entrada_clientes())

    else:
        print("Digite um número válido.")
