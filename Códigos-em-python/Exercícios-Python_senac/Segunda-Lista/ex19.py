nota1 = float(input('primera nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))

media = (((nota2 * 10) * 1) + ((nota2 * 10) * 1) + ((nota3 * 10) * 2)) / 4

if media >= 60:
    print(f'a media é {media}')
    print('APROVADO!!!!!!!')
else:
    print(f'a media é {media}')
    print('REPROVADO!!!!!!')