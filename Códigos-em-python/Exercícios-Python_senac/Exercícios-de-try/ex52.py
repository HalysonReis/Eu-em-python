atleta = str(input('qual o nome do atleta: '))
notas = []

c = 0
while c < 7:
    try:
        nota = float(input(f'qual a nota do {c+1}º jurado:'))
        notas.append(nota)
        c += 1
    except:
        print('digite apenas numero.')

maior = notas[0]
menor = notas[0]
soma = 0

for num in notas:
    soma += num
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

soma = soma - (maior + menor)
notas.remove(maior)
notas.remove(menor)

media = soma / len(notas)

print(f'atleta: {atleta}')
print(f'melhor nota: {maior}')
print(f'pior nota: {menor}')
print(f'media das notas: {media:.2f}')
