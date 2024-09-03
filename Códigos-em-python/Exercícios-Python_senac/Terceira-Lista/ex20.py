terminou = True
p = i = 0

while terminou:
    n = int(input('um numero: '))
    if n == 0:
        terminou = False
    elif n % 2 == 0:
        p += 1
    elif n % 2 == 1:
        i += 1
print('PARES: ', p)
print('IMPARES: ', i)
