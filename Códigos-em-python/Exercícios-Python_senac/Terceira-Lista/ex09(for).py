maior = 0
menor = 0

for num in range(0,10):
    n = int(input('um numero '))
    if num == 0:
        maior = menor = n
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
print("MAOIR: ", maior)
print("MENOR: ", menor)
