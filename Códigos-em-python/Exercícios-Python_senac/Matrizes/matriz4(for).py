numeros = [11, 12, 13, 25, 26, 27, 29, 31, 30,]
matriz = []

print(numeros)

i = 0

linha = []
for c in range(0,3):
    linha.append(numeros[i])
    i += 1
matriz.append(linha)

linha1 = []
for c in range(i, 6):
    linha1.append(numeros[i])
    i += 1
matriz.append(linha1)

linha3 = []
for c in range(i, 9):
    linha3.append(numeros[i])
    i += 1
matriz.append(linha3)

print()
for linha in matriz:
    print(linha)
