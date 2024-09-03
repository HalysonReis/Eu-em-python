def salario_funcionario(horas, preco_hora):
    if horas > 40:
        hora_excedidas = (preco_hora * 1.5) * (horas - 40)

    salario = (40 * preco_hora) + hora_excedidas

    return salario


s = salario_funcionario(44, 50)

print(f' o salario é {s}')