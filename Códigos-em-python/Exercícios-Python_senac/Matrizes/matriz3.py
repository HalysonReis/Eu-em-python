matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
nova_matriz = []
print('primeira matriz')
x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1


l = c = 3

i = 0

while i < l:
    linha = []
    j = 0
    while j < c:
        linha.append(matriz[i][j] * 5)
        j += 1
    nova_matriz.append(linha)
    i += 1

print('segunda matriz')
x = 0
while x < len(matriz):
    print(nova_matriz[x])
    x += 1
