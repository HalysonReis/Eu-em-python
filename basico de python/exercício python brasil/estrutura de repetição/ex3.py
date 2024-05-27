sex = str(input('seu sexo: '))

if sex[0].lower() == 'f':
    print('sexo feminino')
elif sex[0].lower() == 'm':
    print('sexo masculino')
else:
    print('sexo inválido')
    print('só existem dois generos, MASCULINO / FEMININO')