matriz = [
    [2, 3, 0],
    [-1, -2, -4]
]


matriz_inversa = []

j = 0
while j < len(matriz[0]):
    linha = []
    linha.append(matriz[0][j])
    linha.append(matriz[1][j])
    matriz_inversa.append(linha)

    j += 1

for lin in matriz:
    print(lin)
