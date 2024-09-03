n = int(input('um numero: '))

fatorial = 1
for i in range(n, 0, -1):
    fatorial *= i

print(f'o fatorial desse numero é {fatorial}')