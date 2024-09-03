from random import randint


print('você te dado em casa?')

terminou = True

while terminou:
    escolha = str(input('você quer lancar o dado?[s:sim;n;nao] ')).lower()
    dado = randint(1, 6)

    if escolha[0] == 's':
        print('o numero que o dado caiu foi: ', dado)
    else:
        print('até a proxima.')
        terminou = False
        continue
