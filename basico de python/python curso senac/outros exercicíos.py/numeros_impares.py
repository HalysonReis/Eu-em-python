terminou = True
impares = 0

while terminou:
    n = int(input('um numero[999 - para sair]: '))

    if n == 999:
        terminou = False

    elif n % 2 != 0:
        impares += 1

print(f'foram digitados {impares} numeros impares')