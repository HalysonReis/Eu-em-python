ganho_por_hora = float(input('quanto você ganhar por hora: >>> '))
horas_trabalhadas = float(input('quantas horas foram trabalhadas: >>> '))

salario_bruto = ganho_por_hora * horas_trabalhadas

inss = salario_bruto * 0.08

ir = salario_bruto * 0.11

sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (inss + ir + sindicato)

print(f'pago ao inss {inss}')
print(f'pago ao imposto de renda {ir}')
print(f'pago ao sindicato {sindicato}')
print(f'o salario bruto {salario_bruto}')
print(f'o salrio liquido {salario_liquido}')