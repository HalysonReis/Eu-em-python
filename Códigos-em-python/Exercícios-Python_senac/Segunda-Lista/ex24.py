print('[0] para divisão.')
print('[1] para multiplicação.')
print('[2] para somar.')
print('[3] para subtrair.')

escolha = int(input('o que você quer fazer? '))

if escolha > 3:
    print('opção invalida.')

elif escolha == 0:
    n1 = float(input('um numero: '))
    n2 = float(input('um numero: '))

    divisao = n1 / n2

    print(f'a divisão é {divisao}')
elif escolha == 1:
    n1 = float(input('um numero: '))
    n2 = float(input('um numero: '))
    
    divisao = n1 * n2
    
    print(f'a multiplicação é {divisao}')
elif escolha == 2:
    n1 = float(input('um numero: '))
    n2 = float(input('um numero: '))
    
    divisao = n1 + n2
    
    print(f'a soma é {divisao}')
elif escolha == 3:
    n1 = float(input('um numero: '))
    n2 = float(input('um numero: '))

    divisao = n1 - n2
    
    print(f'a subtração é {divisao}')
