terminou = True

soma = 0

c = 0

while terminou:
    idade = float(input('uma idade[0 - para acabar]: '))
    if idade == 0:
        terminou = False
    c += 1
    soma += idade

media = soma / (c - 1)

print(f'a media entre as idade são {media}')