numeros = []

soma = c = 0

while c < 5:
    n = int(input('um numero: '))
    soma += n
    numeros.append(n)
    c += 1

print(f'a soma é {soma}')
print('os numeros digitados são: ')
for n in numeros:
    print(n)