n1 = int(input('um numero: '))
n2 = int(input('um numero: '))
n3 = int(input('um numero: '))

lista = [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]

c1 = 0
c2 = 0
c3 = 0

for num in lista:
    if num == n1:
        c1 += 1
    elif num == n3:
        c2 += 1
    elif num == n3:
        c3 += 1

print(f'{n1}: tem {c1} vezes')
print(f'{n2}: tem {c2} vezes')
print(f'{n3}: tem {c3} vezes')