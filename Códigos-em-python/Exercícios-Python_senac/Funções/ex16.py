def inverte(num):
    num = str(num)

    num_invertido = num[::-1]

    return num_invertido

num = int(input('um numero: '))

invetido = inverte(num)

print(invetido)