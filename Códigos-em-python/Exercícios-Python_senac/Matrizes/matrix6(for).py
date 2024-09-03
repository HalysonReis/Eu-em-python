matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 4],
    [7, 8, 9, 8],
    [7, 8, 9, 6],
]

maior = 0

for lin in matriz:
    soma = 0

    for col in lin:
        soma += col
        if soma > maior:
            maior = soma
print('maior: ', maior)
