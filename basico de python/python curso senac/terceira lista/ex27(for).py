n = int(input('um numero: '))

fatorial = 1
c = n
while c >= n and n > 1:
    fatorial *= n
    n -= 1

print(f'o fatorial desse numero é {fatorial}')