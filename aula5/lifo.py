codigo = 0
fila = []

while True:
    codigo = int(input("Digite um código [1- adicionar; 2- atender; 3- sair; 4- ver pilha]: "))
    if codigo == 3:
        print("Saindo...")
        print(f"A pilha esta assim: {fila}")
        break
    if codigo == 1:
        fila.append(input("Documento para ser adicionado: "))
    elif codigo == 2:
        removendo = fila.pop(-1)
        print(f"Atendendo: {removendo}")
    elif codigo == 4:
        print(f"Pilha: {fila}")
    else:
        print("Digite um codigo válido")
