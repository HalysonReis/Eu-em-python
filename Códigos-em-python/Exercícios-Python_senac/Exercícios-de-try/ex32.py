numeros = []

soma = c = 0

while c < 5:
    try:
        n = int(input('um numero: '))
        soma += n
        numeros.append(n)
        c += 1
    except Exception:
        print('digite apenas numeros.')

print(f'a soma é {soma}')
print('os numeros digitados são: ')
for n in numeros:
    print(n)
