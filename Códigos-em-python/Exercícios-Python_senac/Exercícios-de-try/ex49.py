numeros = []


try:
    terminou = True
    while terminou:
        n = int(input('um numero: '))

        if n == 0:
            terminou = False
            continue

        numeros.append(n)

    soma = 0
    qnt_numeros = len(numeros)
    maxi = max(numeros)
    mini = min(numeros)
    pares = 0
    qnt_pares = 0

    for num in numeros:
        soma += num

        if num % 2 == 0:
            pares += num
            qnt_pares += 1

    media = soma / qnt_numeros

    media_pares = pares / qnt_pares

    print(f'a soma dos numeros é {soma}')
    print(f'a quantidade de numeros digitatos é {qnt_numeros}')
    print(f'a medias dos numeros é {media}')
    print(f'o maior numero digitado foi {maxi}')
    print(f'o menor numero digitado foi {mini}')
    print(f'a media dos pares é {media_pares}')
except ValueError:
    print('digite apenas numeros.')
except ZeroDivisionError:
    print('é impossivel dividir por zero')
