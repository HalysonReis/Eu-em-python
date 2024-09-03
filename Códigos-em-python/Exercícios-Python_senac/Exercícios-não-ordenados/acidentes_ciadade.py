cidades = []
maior = i_maior = 0

menor = i_menor = 0

soma = soma_acidente = 0
c = c2 = 0

while c < 5:
    print('-='*15)
    codigo_cidade = int(input('qual o codigo da cidade: '))
    veiculos_p_cidades = int(input('numeros de veiculos: '))
    num_acidentes = int(input('qual o numeros de acidentes: '))
    print('-='*15)

    cidade = {
        'codigo': codigo_cidade,
        'veiculos': veiculos_p_cidades,
        'acidentes': num_acidentes
    }

    cidades.append(cidade)

    if c == 0:
        maior = menor = cidade['acidentes']
        i_menor = i_maior = c

    else:
        if cidade['acidentes'] > maior:
            maior = cidade['acidentes']
            i_maior = c

        if cidade['acidentes'] < menor:
            menor = cidade['acidentes']
            i_menor = c

    if cidade['veiculos'] < 2000:
        soma_acidente += cidade['acidentes']
        c2 += 1

    soma += cidade['veiculos']
    c += 1


print(f'a cidade com codigo {cidades[i_maior]['codigo']} teve mais acidentes, com {cidades[i_maior]['acidentes']} acidentes.')
print('-='*15)
print(f'a cidade com codigo {cidades[i_menor]['codigo']} teve menos acidentes, com {cidades[i_menor]['acidentes']} acidentes.')
print('-='*15)

media = soma / 5

print(f'a media de veiculos nas cidades são {media}')
print('-='*15)

media2 = soma_acidente / c2

print(f'a media de acidentes nas cidades com menos de 2000 veiculos é {media2}')
