salario_atual = float(input('qual o salário atual: >>> '))
tempo_de_serviço = float(input('tempo de serviço: >>> '))

if salario_atual <= 500:
    reajuste = salario_atual + (salario_atual * 0.25)
    if tempo_de_serviço < 1:
        print('nao tem bonus')
    print(f'o novo saláro é {reajuste} a')

elif salario_atual <= 1000 and salario_atual > 500:
    reajuste = salario_atual + (salario_atual * 0.20)
    if tempo_de_serviço >= 1 and tempo_de_serviço <= 3:
        reajuste += 100
    print(f'o novo saláro é {reajuste} b')

elif salario_atual <= 1500 and salario_atual > 1000:
    reajuste = salario_atual + (salario_atual * 0.15)
    if tempo_de_serviço >= 4 and tempo_de_serviço <= 6:
        reajuste += 200
    print(f'o novo saláro é {reajuste} c')

elif salario_atual <= 2000 and salario_atual > 1500:
    reajuste = salario_atual + (salario_atual * 0.10)
    if tempo_de_serviço >= 7 and tempo_de_serviço <= 10:
        reajuste += 300
    print(f'o novo saláro é {reajuste} e')

elif salario_atual > 2000:
    if tempo_de_serviço > 10:
        salario_atual += 500
    print(f'o novo saláro é {salario_atual} f')