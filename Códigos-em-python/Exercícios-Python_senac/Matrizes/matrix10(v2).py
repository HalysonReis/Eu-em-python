l = c = 3

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

mult = 1

i = j = 0

while i < len(matriz):
    mult *= matriz[i][j]
    i += 1
    j += 1

print('a multiplicação é ', mult)