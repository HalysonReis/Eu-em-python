l = c = 3

i = 0
num = 1

matriz = []

while i < l:
    linha = []
    j = 0
    while j < c:
        linha.append(num)
        j += 1
        num += 1
    matriz.append(linha)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1
