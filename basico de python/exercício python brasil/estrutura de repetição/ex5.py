def nota():
    n1 = float(input('1° nota: '))
    n2 = float(input('2° nota: '))

    media = (n1 + n2) / 2

    if media >= 7:
        print('aprovado')
    elif media < 7:
        print('reprovado')
    elif media == 10:
        print('aprovado com distinção')
