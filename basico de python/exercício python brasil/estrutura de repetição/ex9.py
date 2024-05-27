n1 = int(input('um valor: '))
n2 = int(input('de outro valor: '))
n3 = int(input('mais um valor: '))

menor = n1
meio = n2
maior = n3

if n1 > n2 and n1 > n3:
    maior = n1
if n1 > n2 and n1 < n3:
    meio = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3
if n3 > n1 and n3 < n2:
    meio = n3

print(f'em ordem decrecente fica: {maior}, {meio}, {menor}')

