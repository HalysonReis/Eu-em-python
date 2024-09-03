maior = 0

terminou = True

while terminou:
    n = int(input('um numero: '))
    if n < 0:
        terminou = False
        continue

    if n > maior:
        maior = n

print('o maior numero digitado é: ', maior)