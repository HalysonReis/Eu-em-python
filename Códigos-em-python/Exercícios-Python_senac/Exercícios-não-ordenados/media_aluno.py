n1 = float(input('digite a nota: '))
n2 = float(input('digite a nota: '))
n3 = float(input('digite a nota: '))
n4 = float(input('digite a nota: '))

media = (n1 + n2 + n3 + n4) / 4


if media >= 7:
    print(f'{media}: APROVADO!!!')
elif media < 7 and media >=5:
    print(f'{media}: RECUPERAÇÃO!!!')
else:
    print(f'{media}: REPROVADO!!!')