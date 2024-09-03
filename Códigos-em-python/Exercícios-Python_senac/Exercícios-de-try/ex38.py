try:
    n1 = int(input('um numero: '))
    if n1 < 1:
        raise ZeroDivisionError


    soma = 0
    for i in range(1, n1+1):
        c = 0
        for num in range(1, n1+1):
            if i % num == 0:
                c += 1

        if c == 2:
            soma += i

    print(f'a soma é {soma}')
except ZeroDivisionError:
    print( 'digite um numero maior que zero.')
except Exception as e:
    print('digite apenas numeros')
    print('o numero do erro é ', e.__class__)
    print('a causa é ', e.__cause__)