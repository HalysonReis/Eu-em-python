def positivoNegativo(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    elif num == 0:
        return 0

numero = int(input('um numero: '))

verifica = positivoNegativo(numero)

print('valor retornado', verifica)