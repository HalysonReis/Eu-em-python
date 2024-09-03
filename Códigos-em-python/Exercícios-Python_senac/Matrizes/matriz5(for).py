matriz = []
for lin in range(8):
    linha = []
    for col in range(8):
        linha.append(1)
    matriz.append(linha)

for linha in matriz:
    print(linha)

terminou = True
while terminou:

    print()
    nova_l = int(input('qual linha alterar: '))
    nova_c = int(input('qual coluna alterar: '))

    matriz[nova_l][nova_c] = int(input('digite o numero: '))

    print()
    for linha in matriz:
        print(linha)

    sim = str(input('continuar: '))[0].lower()
    if sim == 'n':
        terminou = False
