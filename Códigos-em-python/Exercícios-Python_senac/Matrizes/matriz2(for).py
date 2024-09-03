matriz = []
for lin in range(3):
    linha = []
    for col in range(3):
        print(f'linha:{lin}, coluna:{col}')
        num = int(input('digite o numero: '))
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print(linha)
