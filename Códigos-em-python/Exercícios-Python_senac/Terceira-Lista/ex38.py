n1 = int(input('um numero: '))
while n1 < 1:
    n = int(input('numero invalido. digite um numero maior que 1: '))

soma = 0
for i in range(1, n1+1):
    c = 0
    for num in range(1, n1+1):
        if i % num == 0:
            c += 1

    if c == 2:
        soma += i

print(f'a soma é {soma}')