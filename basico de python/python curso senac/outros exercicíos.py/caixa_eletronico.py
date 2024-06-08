
nota1 = 0
nota5 = 0
nota10 = 0
nota50 = 0
nota100 = 0

terminou = True
while terminou:
    saque = input('digite o valor do saque[0 - para sair]: ')
    if saque == '0':
        terminou = False
    elif int(saque) > 600 or int(saque) < 10:
        print('valor invalido.')
    else:
        #acima de 100
        if len(saque) == 3:
            #primeiro digito
            if int(saque[-1]) > 5:
                nota5 = 1
                nota1 = int(saque[-1]) - 5
            elif int(saque[-1]) == 5:
                nota5 = 1
            else:
                nota1 = saque[-1]
            #segundo digito
            if int(saque[-2]) > 5:
                nota50 = 1
                nota10 = int(saque[-2]) - 5
            elif int(saque[-1]) == 5:
                nota50 = 1
            else:
                nota10 = saque[-1]

            #terceiro digito
            nota100 = int(saque[0])

            # abaixo de 100
        elif len(saque) == 2:
            #primeiro digito
            if int(saque[-1]) > 5:
                nota5 = 1
                nota1 = int(saque[-1]) - 5
            elif int(saque[-1]) == 5:
                nota5 = 1
            else:
                nota1 = saque[-1]
            #segundo digito
            if int(saque[-2]) > 5:
                nota50 = 1
                nota10 = int(saque[-2]) - 5
            elif int(saque[-1]) == 5:
                nota50 = 1
            else:
                nota10 = saque[-1]

        print(f'Para o saque de {saque} reais, o serão entregues {nota100} notas de 100, {nota50} nota de 50, {nota10} notas de 10, {nota5} nota de 5 e {nota1} nota de 1')