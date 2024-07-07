pessoas = []
s_f = s_m = 0

maior_idade = menor_idade = 0

maior_altura = menor_altura = 0

maior_peso = 0

for i in range(1, 6):
    print('-='*10)
    idade = int(input('qual a idade: '))
    sexo = str(input('qual o sexo: ')).lower()

    if sexo == 'f':
        s_f += 1
    elif sexo == 'm':
        s_m += 1

    altura = int(input('qual a altura: '))
    peso = int(input('qual o peso: '))
    print('-='*10)

    pessoa = {
        'idade': idade,
        'sexo': sexo[0],
        'altura': altura,
        'peso': peso
    }

    pessoas.append(pessoa)



for pessoa in pessoas:
    if pessoa['peso'] > maior_peso:
        maior_peso = pessoa['peso']

    if maior_idade == 0 and maior_idade == 0:
        maior_idade = pessoas[0]['idade']
        menor_idade = pessoas[0]['idade']
    elif pessoa['idade'] > maior_idade:
        maior_idade = pessoa['idade']
    elif pessoa['idade'] < menor_idade:
        menor_idade = pessoa['idade']

    if maior_altura == 0 and menor_altura == 0:
        maior_altura = pessoas[0]['altura']
        menor_altura = pessoas[0]['altura']
    elif pessoa['altura'] > maior_altura:
        maior_altura = pessoa['altura']
    elif pessoa['altura'] < menor_altura:
        menor_altura = pessoa['altura']

print('maior: ', maior_idade)
print('menor: ', menor_idade)
print('maior altura: ', maior_altura)
print('menor altura: ', menor_altura)
print('peso: ', maior_peso)
print('percentual feminino: ', (s_f / len(pessoas)) * 100)
print('percentual masculino: ', (s_m / len(pessoas)) * 100)

# n1 = 500
# n2 = 123
# n3 = (n2 * 100) / n1

# print(n3)
