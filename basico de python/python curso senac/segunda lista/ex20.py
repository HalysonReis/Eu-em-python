nota1 = float(input('nota laboratorio: '))
nota2 = float(input('nota avaliação semestral: '))
nota3 = float(input('nota avaliação bimestral: '))

media = (((nota2 * 10) * 2) + ((nota2 * 10) * 3) + ((nota3 * 10) * 5)) / (2 + 3 + 5)

if media >= 6:
    print(f'a media é {media}')
    print('APROVADO!!!!!!!')
elif media < 6 and media >= 3:
    print(f'a media é {media}')
    print('RECUPERAÇÃO!!!!!!!')
elif media < 3:
    print(f'a media é {media}')
    print('REPROVADO!!!!!!')