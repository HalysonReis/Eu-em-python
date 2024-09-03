valor_tot = 0

terminou = True

valor_tot = compra = float(input('qual o valor do produto: '))

while terminou:

    print('-='*10)
    escolha = str(input('deseja continuar comprando? ')).lower()

    if escolha[0] == 's':
        print('o valor total da comprar é ', valor_tot)
        compra = float(input('qual o valor do produto: '))

        valor_tot += compra
        continue
    elif escolha[0] == 'n':
        print('o valor total da comprar é ', valor_tot)
        terminou = False
        continue
