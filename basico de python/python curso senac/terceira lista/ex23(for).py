n = int(input('um numero: '))

soma = 0

for x in range(1, n):

    if n % x == 0:
        soma += x
        print(x)

print(f'SOMA: {soma}')