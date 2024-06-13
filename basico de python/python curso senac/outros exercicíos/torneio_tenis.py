qnt_criancas = int(input('quantas crianças participaram do torneio? >>> '))

c = 0

grupo_1 = []

grupo_2 = []

grupo_3 = []

continuar = []

while c != qnt_criancas:
    nome_criança = str(input('nome da criança: '))
    pardidas_ganhas = int(
        input(f'{nome_criança}, quantas apartidas ganhas: >>> '))

    if pardidas_ganhas in [5, 6]:
        crianca = {nome_criança: pardidas_ganhas}
        grupo_1.append(crianca)
    elif pardidas_ganhas in [3, 4]:
        crianca = {nome_criança: pardidas_ganhas}
        grupo_2.append(crianca)
    elif pardidas_ganhas in [1, 2]:
        crianca = {nome_criança: pardidas_ganhas}
        grupo_3.append(crianca)
    elif pardidas_ganhas >= 7:
        print('ERRO TENTE NOVAMENTE.')
        continue
    else:
        crianca = {nome_criança: pardidas_ganhas}
        continuar.append(crianca)
    c += 1

print('-=-=-=-= GRUPO 1 =-=-=-=')
for i in grupo_1:
    print(i)

print('-=-=-=-= GRUPO 2 =-=-=-=')
for i in grupo_2:
    print(i)

print('-=-=-=-= GRUPO 2 =-=-=-=')
for i in grupo_3:
    print(i)

print('-=-=-=-= continuar com o treinador =-=-=-=')
for i in continuar:
    print(i)