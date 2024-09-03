p = i = 0
c = 10

for x in range(0, c):
    n = int(input('um numero: '))
    if n == 0:
        break
    elif n % 2 == 0:
        p += 1
    elif n % 2 == 1:
        i += 1
    c += 1
print('PARES: ', p)
print('IMPARES: ', i)
