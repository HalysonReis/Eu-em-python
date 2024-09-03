l = c = 8

i = 0

matriz = []

while i < l:
    linha = []
    j = 0
    while j < c:
        linha.append(1)
        j += 1
    matriz.append(linha)
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1

terminou = True

while terminou:

    print()
    nova_l = int(input('qual linha alterar: '))
    nova_c = int(input('qual coluna alterar: '))

    matriz[nova_l][nova_c] = int(input('digite o numero: '))

    print()
    x = 0
    while x < len(matriz):
        print(matriz[x])
        x += 1

    sim = str(input('continuar: '))[0].lower()
    if sim == 'n':
        terminou = False
