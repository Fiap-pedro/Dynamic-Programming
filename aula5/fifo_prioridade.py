codigo = 0
fila_a_priori = []
fila_b_priori = []

while True:
    codigo = int(input("Digite um código [1- adicionar; 2- atender; 3- sair; 4- ver pilha]: "))
    if codigo == 3:
        print("Saindo...")
        print(f"A pilha esta assim: A.P.:{fila_a_priori}; B.P.:{fila_b_priori}")
        break
    if codigo == 1:
        documento = input("Documento para ser adicionado: ")
        while True:
            prioridade = int(input("É de baixa [0] ou alta prioridade [1]: "))
            if prioridade == 1:
                fila_a_priori.append(documento)
                break
            elif prioridade == 0:
                fila_b_priori.append(documento)
                break
            else:
                print("Código incorreto, insira novamente.")
    elif codigo == 2:
            if fila_a_priori:
                removendo = fila_a_priori.pop(0)
                print(f"Atendendo: {removendo}")
            elif fila_b_priori:
                removendo = fila_b_priori.pop(0)
                print(f"Atendendo: {removendo}")
    elif codigo == 4:
        print(f"Fila de alta prioridade: {fila_a_priori}")
        print(f"Fila de baixa prioridade: {fila_b_priori}")
    else:
        print("Digite um codigo válido")