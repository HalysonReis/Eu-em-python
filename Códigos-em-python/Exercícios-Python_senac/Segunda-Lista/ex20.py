n1 = float(input('nota laboratorio: '))
n2 = float(input('nota avaliação semestral: '))
n3 = float(input('nota avaliação bimestral: '))

if (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10) or (n3 < 0 or n3 > 10):
    print('nota invalida!')
else:
    media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)
    if media >= 6:
        print(f'a media é {media}')
        print('APROVADO!!!!!!!')
    elif media < 6 and media >= 3:
        print(f'a media é {media}')
        print('RECUPERAÇÃO!!!!!!!')
    elif media < 3:
        print(f'a media é {media}')
        print('REPROVADO!!!!!!')
