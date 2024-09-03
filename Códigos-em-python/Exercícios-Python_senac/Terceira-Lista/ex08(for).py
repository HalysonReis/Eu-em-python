soma = 0
for c in range(0,10):
    n = int(input('um numero: '))
    if n % 2 == 0:
        soma += n

print(f'a soma é: {soma/10}')