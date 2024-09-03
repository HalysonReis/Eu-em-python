candidato1 = candidato2 = candidato3 = candidato4 = 0
voto_nulo = voto_branco = 0

total_votos = 0


terminou = True

while terminou:
    print('-='*15)
    print('[1] para candidato 1.')
    print('[2] para candidato 2.')
    print('[3] para candidato 3.')
    print('[4] para candidato 4.')
    print('[5] para voto nulo.')
    print('[6] para voto em branco.')
    print('[0] para sair.')
    print()

    votar_em = int(input('em qual canditado votar: '))
    print('-='*15)

    match votar_em:
        case 1:
            candidato1 += 1
        case 2:
            candidato2 += 1
        case 3:
            candidato3 += 1
        case 4:
            candidato4 += 1
        case 5:
            voto_nulo += 1
        case 6:
            voto_branco += 1
        case 0:
            terminou = False
            continue
        case __:
            print('voto invalido.')
            continue
    
    total_votos += 1

print(
    f'voto candidato 1: {candidato1}\nvoto candidito 2: {candidato2}\nvoto candidato 3: {candidato3}\nvoto candidato: {candidato4}\nvoto nulo: {voto_nulo}\nvoto em branco: {voto_branco}'
)

percentual_nulo = total_votos * (voto_nulo / 100)
percentual_branco = total_votos * (voto_branco / 100)

print('o total de votos é ', total_votos)

print('percentual votos nulos: ', percentual_nulo)
print('percentual votos nulos: ', percentual_branco)
