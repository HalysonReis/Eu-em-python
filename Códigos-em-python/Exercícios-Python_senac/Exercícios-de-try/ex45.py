try:
    salario_carlos = int(input('qual o salario do carlos: R$'))

    salario_joao = salario_carlos / 3

    inves_carlos = salario_carlos
    inves_joao = salario_joao

    print('investimento inicial carlos: ', inves_carlos)
    print('investimento inicial joão: ', inves_joao)

    c = 0
    while inves_joao <= inves_carlos:
        inves_carlos *= 1.02
        inves_joao *= 1.05
        print('-='*10)
        print('CARLOS: ', inves_carlos)
        print('JOÃO: ', inves_joao)
        print('-='*10)

        c += 1

    print(f'foram necessarios {c} meses para joão ultrapassar carlos')
except ZeroDivisionError:
    print('oh jumento, como eu vou calcular se você digitou zero.')
except Exception as e:
    print('digite apenas numeros.')
    print('o erro é ', e.__class__)
