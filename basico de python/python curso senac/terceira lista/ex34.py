vetor = []
veotor_par = []
veotor_impares = []

c = 0

while c < 20:
    n = int(input('um numero:'))

    vetor.append(n)

    if n % 2 == 0:
        veotor_par.append(n)
    elif n % 2 != 0:
        veotor_impares.append(n)

    c += 1

print(f'os numeros digitados são: {vetor}')
print(f'os numeros digitados impares são: {veotor_impares}')
print(f'os numeros digitados par são: {veotor_par}')