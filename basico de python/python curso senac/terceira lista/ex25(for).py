soma = c = 0
infinito = 10

for x in range(0 , infinito):
    idade = float(input('uma idade[0 - para acabar]: '))
    if idade == 0:
        break
    c += 1
    infinito += 1
    soma += idade

media = soma / (c - 1)

print(f'a media entre as idade são {media}')