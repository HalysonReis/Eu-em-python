horas_normais = float(input('quantas horas nomais foram trabalhadas? '))
horas_extras = float(input('quantas horas extras foram trabalhadas? '))

salario_bruto = horas_normais + horas_extras
print(f'o salário bruto é R${salario_bruto}')

salario_liquido = salario_bruto - (salario_bruto *0.11)
print(f'o salário liquido é R${salario_liquido}')
