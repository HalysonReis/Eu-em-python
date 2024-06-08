n = int(input('um numero: '))

fatorial = 1
for i in range(1, n +1):
    fatorial *= i

print(f'o fatorial desse numero é {fatorial}')