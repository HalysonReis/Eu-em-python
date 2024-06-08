comprar = int(input('oque você quer comprar:1|lata;2|galão >>> '))
qnt = int(input('qual a quantidade: >>> '))

if comprar == 1:
    print(f'você vai pagar {qnt * 80}')
elif comprar == 2:
    print(f'você vai pagar {qnt * 25}')