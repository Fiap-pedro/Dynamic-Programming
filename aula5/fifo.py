fila = []

while True:
    cliente = input("nome ['FIM' para sair]:")
    if cliente == 'FIM':
        break
    else:
        fila.append(cliente)

print(fila)
while fila:
    atendido = fila.pop(0)
    print(f"Atendendo: {atendido}")

print("Todos os clientes foram atendidos.")

