valor_produto = float(input('valor do produto: '))
estado_destinado = str(input('estado destinado: ')).upper()

match estado_destinado:
    case 'MG':
        print(f'o valor total do produto é {valor_produto +(valor_produto * 0.07)}')
    case 'SP':
        print(f'o valor total do produto é {valor_produto +(valor_produto * 0.12)}')
    case 'RJ':
        print(f'o valor total do produto é {valor_produto +(valor_produto * 0.15)}')
    case 'MS':
        print(f'o valor total do produto é {valor_produto +(valor_produto * 0.08)}')
    case __:
        print('estado inválido!!!!')