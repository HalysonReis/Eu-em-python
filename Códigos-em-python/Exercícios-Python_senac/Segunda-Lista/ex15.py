horas = int(input('quantas horas trabalhadas no mês: '))

salario = horas * 40.5

if salario > 2500:
    salario_liquido = salario - (salario * 0.11)
    print(f'o salário liquido é {salario_liquido}')
else:
    print(f'o salário liquido é {salario}')