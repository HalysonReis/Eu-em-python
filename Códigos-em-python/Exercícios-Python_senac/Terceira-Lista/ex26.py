n1 = int(input('um numero: '))
n2 = int(input('outro numero: '))

mult = n1
c = n2

while c > 1:
    c -= 1
    mult *= n1

print(f'{n1} elevado a {n2} = {mult}')