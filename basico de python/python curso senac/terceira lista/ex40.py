n1 = int(input('um numero: '))

n2 = int(input('outro numero: '))


soma = 0
if n1 >= n2:
    print('numero invalido.')
else:
    for i in range(n1, n2+1):
        if i % 2 != 0:
            print('IMPAR: ', i)
            soma += i

print('a soma dos impares é ', soma)