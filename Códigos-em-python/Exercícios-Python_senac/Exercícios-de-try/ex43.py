import random

acertar = random.randint(1, 99)

tentativas = 0

print('vamos jogar um jogo.')
print('tente adivinhar o numero escolido')


terminou = True
while terminou:
    try:
        n = int(input('digite o numero:'))
        tentativas += 1

        if n == acertar:
            print('você acertou.')
            terminou = False
            continue

        elif n < acertar:
            print('é um numero maior.')

        elif n > acertar:
            print('é um numero menor.')
    except:
        print('digite um numero, oh burro.')
        print('como você vai adivinhar o numero se não digitar um numero? Ein?')