
soma = 0

terminou = True

while terminou:
    n = int(input('um numero: '))
    if n < 0:
        print('terminando o programa.')
        terminou = False
        continue

    soma += n

print('a soma é ', soma)
