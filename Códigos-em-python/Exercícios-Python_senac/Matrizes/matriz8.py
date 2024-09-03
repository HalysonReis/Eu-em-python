matriz = [
    [11, 132, 13, 21],
    [19, 199, 17, 22],
    [45, 20, 27, 15],
    [16, 14, 14, 29]
]

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