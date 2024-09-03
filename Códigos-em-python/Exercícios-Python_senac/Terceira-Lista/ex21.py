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

while menor <= maior:
    if menor % 2 == 0:
        soma += menor
    elif menor % 2 == 1:
        mult = mult * menor
    menor += 1


print('soma dos pares',soma)
print('multiplicação dos impares',mult)