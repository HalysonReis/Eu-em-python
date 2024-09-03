soma = 0
c = 0 
while c != 10:
    n = int(input('um numero: '))
    if n > 0:
        soma += n
        print(n)
    c += 1
print(f'a soma é: {soma}')