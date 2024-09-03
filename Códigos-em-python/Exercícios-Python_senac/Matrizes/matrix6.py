matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 4],
    [7, 8, 9, 8],
    [7, 8, 9, 6],
]

maior = 0

x = 0

while x < len(matriz):
    j = 0

    soma = 0

    while j < len(matriz[x]):
        soma += matriz[x][j]
        if soma > maior:
            maior = soma
        j += 1
    x += 1

print('maior: ', maior)
