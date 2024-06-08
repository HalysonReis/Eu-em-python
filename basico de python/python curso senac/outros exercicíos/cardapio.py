conta_total = 0

while True:
    print()
    print('-='* 10)
    print('[1] - Rosbife, R$200,00')
    print('[2] - Marmita, R$50,00')
    print('[3] - Lanen, R$100,00')
    print('[4] - Churrasco, R$150,00')
    print('[5] - Macarão, R$250,00')
    print('[6] - para parar de fazer pedido')
    print('-='* 10)


    print()
    #fazendo o pedido
    pedido = input('o que o senhor deseja? ')

    pedido = int(pedido)
    
    match pedido:
        case 1:
            print('-='* 10)
            qnt = int(input('qual a quantidade: '))
            conta_total += 200 * qnt

        case 2:
            print('-='* 10)
            qnt = int(input('qual a quantidade: '))
            conta_total += 50 * qnt
            
        case 3:
            print('-='* 10)
            qnt = int(input('qual a quantidade: '))
            conta_total += 100 * qnt
            
        case 4:
            print('-='* 10)
            qnt = int(input('qual a quantidade: '))
            conta_total += 150 * qnt
            
        case 5:
            print('-='* 10)
            qnt = int(input('qual a quantidade: '))
            conta_total += 250 * qnt
        case 6:
            break
        case __:
            print('numero invalido.')

print()
print('-='* 10)
print('conta total: ', conta_total)
print()

pagar_garcon = input('deseja pagar 10% ao garçon? ').lower()

if pagar_garcon[0] == 's':
    conta_total = conta_total * 1.1 

print('-='* 10)

print('deve ser pago um total de ', conta_total)