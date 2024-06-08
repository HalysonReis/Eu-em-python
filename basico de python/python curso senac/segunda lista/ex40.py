from math import sqrt

a = int(input('um numero: '))
b = int(input('um numero: '))
c = int(input('um numero: '))

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print('não existe raiz')
elif delta == 0:
    print('existe raiz')
elif delta >= 0:
    x1 = (-b - sqrt(delta)) / 2 * a
    x2 = (-b + sqrt(delta)) / 2 * a
    print('existe raiz')
    print(f'a primera raiz é {x1}')
    print(f'a segunda raiz é {x2}')
