n1 = int(input('preço do produto: '))
n2 = int(input('de outro produto: '))
n3 = int(input('mais um protudo: '))

if n1 < n2 and n1 < n3:
    print(f'o primeiro produto é o mais barato, custando {n1}')
elif n2 < n3:
    print(f'o segundo produto é o mais barato, custando {n2}')
elif n3 < n2:
    print(f'o terceiro produto é o mais barato, custando {n1}')
elif n3 < n1:
    print(f'o terceiro produto é o mais barato, custando {n1}')
else:
    print('o preço de todos os produtos são iguais')