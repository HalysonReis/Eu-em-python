matriz = [
    [12, 11, 16],
    [17, 13, 14],
    [15, 24, 26]
]

lista = []

for lin in matriz:

    for col in lin:
        if col % 2 == 0:
            lista.append(col)

print('os pares', lista)