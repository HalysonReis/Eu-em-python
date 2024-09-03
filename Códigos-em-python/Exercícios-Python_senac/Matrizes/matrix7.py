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

while i < len(x):
    linha = []

    j = 0
    while j < len(x[i]):
        linha.append(x[i][j]+y[i][j])
        j += 1
    z.append(linha)
    i += 1

c = 0

while c < len(z):
    print(z[c])
    c += 1