l = 3
c = 3

i = 0

x = []
print('primeira matriz.')
while i < l:
    linha = []
    j = 0
    while j < c:
        print(f'linha:{i}, coluna:{j}')
        num = int(input('digite o numero: '))
        linha.append(num)
        j += 1
    x.append(linha)
    i += 1

l2 = 3
c2 = 3

i = 0

y = []
print('segunda matriz.')
while i < l2:
    linha = []
    j = 0
    while j < c2:
        print(f'linha:{i}, coluna:{j}')
        num = int(input('digite o numero: '))
        linha.append(num)
        j += 1
    y.append(linha)
    i += 1

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
