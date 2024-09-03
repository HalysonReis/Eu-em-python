terminou = True

while terminou:
    n = int(input('um numero[0 para sair]:'))
    if n <= 0:
        print('saindo...')
        terminou = False
        continue

    if n % 2 == 0:
        print('o numero digitado é par')
    elif n % 2 != 0:
        print('o numero digita é impar')

