l = 2
c = 3

i = 0

matriz = []

while i < l:
    linha = []
    j = 0
    while j < c:
        print(f'linha:{i}, coluna:{j}')
        num = int(input('digite o numero: '))
        linha.append(num)
        j += 1
    matriz.append(linha)
    i += 1

matriz_inversa = []

j = 0
while j < len(matriz[0]):
    linha = []
    linha.append(matriz[0][j])
    linha.append(matriz[1][j])
    matriz_inversa.append(linha)

    j += 1

c = 0

while c < len(matriz_inversa):
    print(matriz_inversa[c])
    c += 1
