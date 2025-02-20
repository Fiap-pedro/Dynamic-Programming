tabelaClima = """
1 - Ensolarado
2 - Chuvoso
3 - Nublado
4 - Nevando
"""
print(tabelaClima)

clima = int(input("Como está seu dia hoje de acordo com a tabela ? "))

if clima == 1:
    print("Dia de futebol e churrasco.")
elif clima == 2:
    print("Dia de filme e série.")
elif clima == 3:
    print("Dia de ler um livro.")
elif clima == 4:
    print("Ótimo dia para tomar um café ou chocolate.")
else:
    print("Número inexistente na tela")
