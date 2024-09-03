l = 4
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
