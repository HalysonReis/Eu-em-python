n = int(input('um numero: '))
while n < 1:
    n = int(input('numero invalido. digite um numero maior que 1: '))

c = 1
for i in range(1, n):
    if n % i == 0:
        c += 1

if c == 2:
    print('é primo')
else:
    print('não é primo')