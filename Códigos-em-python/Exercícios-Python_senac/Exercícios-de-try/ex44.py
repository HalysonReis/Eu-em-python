terminou = True

while terminou:
    print()
    print('-='*15)
    print('[1] para adição')
    print('[2] para subitração')
    print('[3] para multiplicação')
    print('[4] para divisão')
    print('[5] para sair')

    try:
        escolha = int(input('qual a opção escolhida: --> '))

        match escolha:
            case 1:
                n1 = int(input('digite um numero: '))
                n2 = int(input('digite outro numero: '))

                soma = n1 + n2

                print()
                print(f'{n1} + {n2} = {soma}')
                print()
            case 2:
                n1 = int(input('digite um numero: '))
                n2 = int(input('por qual numero você quer subtrair: --> '))

                sub = n1 - n2

                print()
                print(f'{n1} - {n2} = {sub}')
                print()
            case 3:
                n1 = int(input('digite um numero: '))
                n2 = int(input('digite outro numero: '))

                mult = n1 * n2

                print()
                print(f'{n1} X {n2} = {mult}')
                print()
            case 4:
                try:
                    n1 = int(input('digite um numero: '))
                    n2 = int(input('digite o numero que sera feita a divisão: '))
                    if n2 == 0:
                        raise ZeroDivisionError

                    div = n1 / n2

                    print()
                    print(f'{n1} X {n2} = {div}')
                    print()
                except ZeroDivisionError:
                    print('divisão por zero não é permitida.')
                except:
                    print('valores invalidos.')
            case 5:
                terminou = False
                print('TCHAUUUU')
                continue
    except:
        print('digite o valor correto.')
