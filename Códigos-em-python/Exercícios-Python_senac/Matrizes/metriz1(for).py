matriz = []
num = 0
for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(num)
        num += 1
    matriz.append(linha)

for linha in matriz:
    print(linha)
