n1 = int(input('um numero:'))
n2 = int(input('outro numero:'))

intervalo = 0

menor = 0

if n1 > n2:
    menor = n2
    intervalo = n1 - n2
else:
    menor = n1
    intervalo = n2 - n1

soma = 0
mult = 0

c = 0
while c <= intervalo:
    if menor % 2 == 0:
        soma += menor
    elif menor % 2 == 1:
        mult *= menor
    menor += 1
    c += 1

print(soma)
print(mult)