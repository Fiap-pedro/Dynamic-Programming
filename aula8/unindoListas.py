pessoas = []


def cadastro():
    pessoa = []

    nome = pessoa.append(input("Nome: "))
    idade = pessoa.append(input("Idade: "))
    sexo = pessoa.append(input("Sexo: "))

    return pessoa


for i in range(3):
    pessoas.append(cadastro())

print(pessoas)
