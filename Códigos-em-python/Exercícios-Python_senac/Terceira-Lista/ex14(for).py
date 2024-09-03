n = int(input('um numro: '))
if n % 2 == 0:
    for x in range(0, n+1, 2):
        print(f'pares: {x}')
else:
    print('numero invalido.')