idade = int(input('qual a idade? '))
teste_psicotecnico = str(input('qual o resultado no testa psicotecnico? '))
prova_teórica = float(input('qual a nota na prova? '))

if idade >= 18:
    print('tem idade para tirar CNH.')
    if teste_psicotecnico == 'aprovado' and prova_teórica >= 7.0:
        print('esta apto.')
    elif teste_psicotecnico == 'reprovado' or prova_teórica < 7.0:
        print('nao esta apto.')
else:
    print('não tem idade.')