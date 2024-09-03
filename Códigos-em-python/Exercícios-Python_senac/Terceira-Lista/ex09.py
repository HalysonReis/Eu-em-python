n = int(input('um numero '))
maior = n
menor = n
c = 0

while c != 9:
    n = int(input('um numero '))
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    c += 1
print("MAOIR: ", maior)
print("MENOR: ", menor)
