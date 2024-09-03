num = input('um numero: ')

if int(num) > 0:
    soma = 0
    for i in num:
        soma += int(i)
    print(f'a soma dos algarismos é {soma}')
else:
    print('numero invalido.')