matriz = [
    [11, 132, 13, 21],
    [19, 199, 17, 22],
    [45, 20, 27, 15],
    [16, 14, 14, 29]
]

tot = 0

lista = []


for lin in matriz:

    for col in lin:
        if col > 20:
            tot += 1
            lista.append(col)

print('o total é ', tot)

print('os numeros são: ', lista)