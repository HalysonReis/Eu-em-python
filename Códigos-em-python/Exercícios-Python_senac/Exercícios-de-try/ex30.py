maior = 0
menor = 0
terminou = True

while terminou:
    try:
        n = int(input('um numero: '))
        if n < 0:
            terminou = False
            continue
        if menor == 0:
            maior = menor = n
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    except Exception:
        print('digite apenas numeros')
print("MAOIR: ", maior)
print("MENOR: ", menor)
