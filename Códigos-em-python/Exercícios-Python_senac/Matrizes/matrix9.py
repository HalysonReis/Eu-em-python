matriz = [
    [12, 11, 16],
    [17, 13, 14],
    [15, 24, 26]
]

lista = []

i = 0

while i < len(matriz):
    j = 0

    while j < len(matriz[i]):
        if matriz[i][j] % 2 == 0:
            lista.append(matriz[i][j])
        j += 1

    i += 1

print('os pares', lista)