matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print('primeira matriz')
for linha in matriz:
    print(linha)

nova_matriz = []

for lin in matriz:
    linha = []
    for col in lin:
        col = col * 5
        linha.append(col)
    nova_matriz.append(linha)

print('segunda matriz')
for linha in nova_matriz:
    print(linha)
