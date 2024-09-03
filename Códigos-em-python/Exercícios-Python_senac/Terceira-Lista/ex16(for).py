n = int(input('um numro: '))
if n % 2 == 1:
    for x in range(1, n+1, 2):
        print(f'pares: {x}')
else:
    print('numero invalido.')