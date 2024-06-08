n1 = int(input('um numero: '))
n2 = int(input('um numero: '))
n3 = int(input('um numero: '))

if n1 > n2:
    print('não esta em ordem crescente.')
elif n2 > n1 and n3 > n2:
    print('está em ordem crescente.')
else:
    print('não está em ordem crescente.')