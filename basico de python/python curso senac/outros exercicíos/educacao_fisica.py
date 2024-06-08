alunos = []

h_feminino = 0

masculino = 0

bons = 0

c = 10
while c >= 0:
    c -= 1
    matricula = input('matrícula: ')
    sexo = input('sexo| M/F: ').lower()
    altura = int(input('altura(CM): '))
    status = int(input('status fisíco[1 - bom, 2 - regular, 3 - ruim]: '))

    while status not in ['1', '2', '3']:
        status = input('status fisíco[1 - bom, 2 - regular, 3 - ruim]: ')

    aluno = {
        'matricula': matricula,
        'sexo': sexo,
        'altura': altura,
        'status': status
    }
    alunos.append(aluno)

    if int(aluno['altura']) > 170:
        h_feminino += 1
    if aluno['sexo'] == 'm':
        masculino += 1
        if aluno['status'] == 1:
            bons += 1
    

porcentagem =   (bons * 100) / masculino

print(f'alunas femininas com mais 1,70 metros {h_feminino}')
print(f'porcentagem de alunos masculinos com bom fisícos {porcentagem}')