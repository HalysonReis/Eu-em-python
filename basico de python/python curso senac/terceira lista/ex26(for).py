n1 = int(input('um numero: '))
n2 = int(input('outro numero: '))

mult = n1
for x in range(0, n2-1):
    mult *= n1

print(f'{n1} elevado a {n2} = {mult}')