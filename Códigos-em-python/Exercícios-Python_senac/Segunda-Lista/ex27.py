print('[1] somar dois numeros.')
print('[2] diferença entre dois numeros.')
print('[3] produto entre dois numeros.')
print('[4] divisão entre dois numeros.')

print('-='* 30)

escolha = int(input('escolha uma opção: >>> '))

print('-='* 30)

match escolha:
    case 1:
        n1 = float(input('um numero: '))
        n2 = float(input('outro numero: '))
        soma = n1 + n2
        print(f'a soma dos respectivos numeros é: {soma}')
    case 2:
        n1 = float(input('um numero: '))
        n2 = float(input('outro numero: '))
        menor = 0
        maior = 0
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print(f'{maior} - {menor} = {maior - menor}')
    case 3:
        n1 = float(input('um numero: '))
        n2 = float(input('outro numero: '))
        produto = n1 * n2
        print(f'{n1} X {n2} = {produto}')
    case 4:
        n1 = float(input('digite o denominador: '))
        n2 = float(input('um numero: '))

        while n1 <= 0:
            print('o numero tem que ser maior que 0.')
            n2 = float(input(f'denominador do numero {n1}: '))
        print(f'{n1} / {n2} = {n1 / n2}')
    case __:
        print('ERRO NUMERO INVALIDO!!!!!!')