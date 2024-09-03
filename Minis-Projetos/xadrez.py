black = '\033[37m'
blue_bg = '\033[44m'
red = '\033[31m'
blue = '\033[34m'
fim = '\033[0m'
bold = '\033[1m'

l = c = 8

matriz = []

for lin in range(0, 8):
    linha = []
    if lin == 0:
        linha.append('to')
        linha.append('ca')
        linha.append('bi')
        linha.append('ra')
        linha.append('Re')
        linha.append('bi')
        linha.append('ca')
        linha.append('to')

    elif lin == 7:
        linha.append('to')
        linha.append('ca')
        linha.append('bi')
        linha.append('RE')
        linha.append('ra')
        linha.append('bi')
        linha.append('ca')
        linha.append('to')
    for col in range(0, 8):
        if lin == 1:
            linha.append(f'q{col+1}')
        if lin == 6:
            linha.append(f'p{col+1}')
        elif lin in [2, 3, 4, 5]:
            linha.append('__')
    matriz.append(linha)

print(blue_bg)

print('col',
      [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7'],
      )
print('lin    |     |     |     |     |     |     |     |  ')

x = 0
for linha in matriz:
    print(x, '-', linha)
    x += 1

print(fim)

terminou = True

while terminou:
    try:
        # jogada das brancas
        print('jogo das brancas.')
        print('informe a linha e coluna que está a peça')
        print('a qualquer momento digite -1 para sair.')

        lin_branca = int(input('LINHA: '))
        if lin_branca < 0:
            raise ZeroDivisionError
        col_branca = int(input('COLUNA: '))
        if col_branca < 0:
            raise ZeroDivisionError

        print('informe a linha e coluna para mover')

        mov_lin_branca = int(input('LINHA: '))
        mov_col_branca = int(input('COLUNA: '))

        temp = '__'
        print(temp)
        matriz[mov_lin_branca][mov_col_branca] = matriz[lin_branca][col_branca]
        matriz[lin_branca][col_branca] = temp


        #print matriz apos jogada das brancas
        print(blue_bg)

        print('col',
            [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7'],
            )
        print('lin    |     |     |     |     |     |     |     |  ')

        x = 0
        for linha in matriz:
            print(x, '-', linha)
            x += 1

        print(fim)


        # jogada das pretas
        print('jogo das pretas.')
        print('a qualquer momento digite -1 para sair.')
        print('informe a linha e coluna que está a peça')

        lin_preta = int(input('LINHA: '))
        if lin_preta < 0:
            raise ZeroDivisionError
        col_preta = int(input('COLUNA: '))
        if col_preta < 0:
            raise ZeroDivisionError

        print('informe a linha e coluna para mover')

        mov_lin_preta = int(input('LINHA: '))
        mov_col_preta = int(input('COLUNA: '))

        temp = '__'
        matriz[mov_lin_preta][mov_col_preta] = matriz[lin_preta][col_preta]
        matriz[lin_preta][col_preta] = temp

        #print apos jogada das pretas
        print(blue_bg)

        print('col',
            [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7'],
            )
        print('lin    |     |     |     |     |     |     |     |  ')

        x = 0
        for linha in matriz:
            print(x, '-', linha)
            x += 1

        print(fim)

    except ZeroDivisionError:
        terminou = False
        continue
    except Exception as e:
        print('ocorreu um erro.')
        print('o erro é ', e.__class__)
