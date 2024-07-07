n1 = int(input('um numero:'))
n2 = int(input('outro numero:'))

menor = 0
maior = 0

if n1 > n2:
    menor = n2
    maior = n1
else:
    menor = n1
    maior = n2

soma = 0
mult = 1

for c in range(menor, maior+1, 1):
    if c % 2 == 0:
        soma += c
    elif c % 2 == 1:
        mult = mult * c


print('soma dos pares',soma)
print('multiplicação dos impares',mult)