nota1 = float(input('qual primeira nota do aluno: '))
nota2 = float(input('qual segunda nota do aluno: '))

if nota1 >= 0 and nota1 <= 10:
    if nota2 >=0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f'a meidia das notas são: {media}')
    else:
        print('notas invalidas.')
else:
    print('notas invalidas.')