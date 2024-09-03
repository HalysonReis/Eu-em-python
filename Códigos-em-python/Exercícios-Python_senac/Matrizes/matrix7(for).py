x = [
    [40, 30, 20],
    [17, 16, 14],
    [19, 15, 18]
]

y = [
    [31, 32, 33],
    [21, 22, 23],
    [12, 13, 19]
]

z = []

i = 0

for lin in x:
    linha = []

    j = 0
    for col in lin:
        linha.append(lin[j]+y[i][j])
        j += 1
    z.append(linha)
    i += 1

for lin in z:
    print(lin)
