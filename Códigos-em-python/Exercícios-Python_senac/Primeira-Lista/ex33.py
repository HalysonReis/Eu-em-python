from math import sqrt

a = float(input('um numero: '))
b = float(input('outro numero: '))

raiz = sqrt((a**2) + (b**2))

print(f'a hipotenusa é {raiz:.2f}')