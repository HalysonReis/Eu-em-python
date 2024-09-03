from math import sqrt

num = int(input('um numero: '))

if num > 0:
    print(f'a raiz quadrada de {num} é {sqrt(num)}')
elif num < 0:
    print('numero negativo.')
else:
    print('numero igual a zero.')