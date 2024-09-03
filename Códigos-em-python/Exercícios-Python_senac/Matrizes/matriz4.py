numeros = [11, 12, 13, 25, 26, 27, 29, 31, 30,]
matriz = []

print(numeros)

i = 0

linha = []
while i < 3:
    linha.append(numeros[i])
    i += 1
matriz.append(linha)

linha1 = []
while i < 6:
    linha1.append(numeros[i])
    i += 1
matriz.append(linha1)

linha3 = []
while i < 9:
    linha3.append(numeros[i])
    i += 1
matriz.append(linha3)

print()
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1
