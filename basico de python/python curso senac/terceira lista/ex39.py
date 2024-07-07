n1 = int(input('um numero: '))
while n1 < 1:
    n = int(input('numero invalido. digite um numero maior que 1: '))

n2 = int(input('um numero: '))
while n2 < 1 or n2 < n1:
    n2 = int(input(f'numero invalido. digite um numero maior que 1 ou maior que {n1}: '))

for i in range(n1, n2+1):
    c = 0
    for num in range(1, n2+1):
        if i % num == 0:
            c += 1

    if c == 2:
        print(i, ' é primo')
