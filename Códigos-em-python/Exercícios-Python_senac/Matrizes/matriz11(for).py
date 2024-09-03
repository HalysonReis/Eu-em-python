matriz = [
    [5, -8, 10],
    [1, 2, 15],
    [25, 10, 7]
]

col1 = col2 = col3 = 0

lista = []

i = 0

for lin in matriz:
    j = 0

    for col in lin:
        if j == 0:
            col1 += col
        elif j == 1:
            col2 += col
        elif j == 2:
            col3 += col
        j += 1

    i += 1

lista.append(col1)
lista.append(col2)
lista.append(col3)

print('a soma é ',lista)