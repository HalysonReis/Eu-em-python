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

tot = 0

lista = []

i = 0

while i < len(matriz):
    j = 0

    while j < len(matriz[i]):
        if matriz[i][j] > 20:
            tot += 1
            lista.append(matriz[i][j])
        j += 1

    i += 1

print('o total é ', tot)

print('os numeros são: ', lista)