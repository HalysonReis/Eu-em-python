codigo_produto = int(input('qual o codigo do produto? >>> '))
qnt_produto = int(input('qual a quantidade do produto? >>> '))

match codigo_produto:
    case 100:
        print(f'serão entreges {qnt_produto} Hot Dogs')
    case 102:
        print(f'serão entreges {qnt_produto} X-saladas')
    case 103:
        print(f'serão entreges {qnt_produto} X-bacon')
    case 104:
        print(f'serão entreges {qnt_produto} X-burguer')
    case 105:
        print(f'serão entreges {qnt_produto} suco de laranja')
    case 106:
        print(f'serão entreges {qnt_produto} refrigerante')
    case __:
        print(f'"{codigo_produto}" este codigo está errado.')
