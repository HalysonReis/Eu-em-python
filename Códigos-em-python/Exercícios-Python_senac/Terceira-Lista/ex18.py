qnt = int(input('quantos numeros você quer digitar? '))
n = int(input('um numero '))
maior = n
menor = n
c = 0

while c != qnt - 1:
    n = int(input('um numero '))
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    c += 1
print("MAOIR: ", maior)
print("MENOR: ", menor)
