salario = float(input('qual é o seu salário? '))
emprestimo = float(input('qual o valor do emprestimo? '))

porcent_salario = salario * 0.2

if emprestimo > porcent_salario:
    print('emprestimo nagado.')
else:
    print('emprestimo aprovado.')