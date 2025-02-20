tabela = """
1 - cilindro
2 - retângulo
"""
print(tabela)
figura = int(input("Qual figura quer ver a área ?"))

if figura == 1:
    r = float(input("Raio: "))
    h = float(input("Altura: "))

    pi = 3.1415
    areaCilindro = 2*pi*r*(r+h)
    volumeCilindro = pi * r**2 * h

    print(f"A área do cilindro é igual à {areaCilindro:.2f}")
    print(f"O volume do cilindro é igual à {volumeCilindro:.2f}")

elif figura == 2:
    b = float(input("Base: "))
    h = float(input("Altura: "))
    l = float(input("Largura"))

    areaRetangulo = b * h
    volumeRetangulo = b * h * l

    print(f"O volume do retângulo é igual à {volumeRetangulo:.2f}")
    print(f"A área do retângulo é igual à {areaRetangulo:.2f}")

else:
    print("número incorreto.")
