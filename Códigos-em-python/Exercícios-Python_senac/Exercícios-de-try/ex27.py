try:
    n = int(input('um numero: '))

    fatorial = 1
    for i in range(n, 0, -1):
        fatorial *= i

    print(f'o fatorial desse numero é {fatorial}')
except Exception:
    print('erros no codigo.')
    print('o erro é ', Exception.__class__)