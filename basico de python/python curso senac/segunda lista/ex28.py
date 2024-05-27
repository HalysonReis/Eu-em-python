idade = int(input('sua idade: '))
tempo_trabalho = int(input('seu tempo de trabalho: '))

if idade < tempo_trabalho:
    print('idade inválida.')
    while idade < tempo_trabalho:
        idade = int(input('sua idade: '))
        tempo_trabalho = int(input('seu tempo de trabalho: '))
if idade >= 65:
    print('você pode se aposentar.')
elif tempo_trabalho >= 30:
    print('você pode se aposentar')
elif idade >= 60 and tempo_trabalho >= 25:
    print('você pode se aposentar.')
else:
    print('você não pode se aposentar.')
