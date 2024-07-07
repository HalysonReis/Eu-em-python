alunos = []


for i in range(1, 11):
    print()
    print(f'-=-=-=-=- {i}º aluno -=-=-=-=-=-')
    nota1 = int(input('1º nota: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input('nota invalida. digite a nota certa: '))

    nota2 = int(input('2º nota: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input('nota invalida. digite a nota certa: '))

    nota3 = int(input('3º nota: '))
    while nota3 < 0 or nota3 > 10:
        nota3 = int(input('nota invalida. digite a nota certa: '))

    nota4 = int(input('4º nota: '))
    while nota4 < 0 or nota4 > 10:
        nota4 = int(input('nota invalida. digite a nota certa: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    aluno = {
        i: media
    }
    alunos.append(aluno)

print()

c = 1
for aluno in alunos:
    print(f'media do {c}º aluno: {aluno[c]}')
    c += 1
