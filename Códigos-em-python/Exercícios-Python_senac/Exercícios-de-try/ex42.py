terminou = True

while terminou:
    try:
        n = int(input('digite um numero:'))

        if n <= 0:
            terminou = False
            continue
        else:
            cubo = n ** 3
            quadrado = n ** 2
            raiz = n ** 0.5

            print(f'\n-=-=-=-=-= o numero é {n} -=-=-=-=-=-=')
            print('quadrado: ', quadrado)
            print('cubo: ', cubo)
            print('raiz: ', raiz)
    except Exception:
        print('digite apenas numeros.')