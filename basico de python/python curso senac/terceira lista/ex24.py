c = 1000

soma = 0

while c > 0:
    if str(c)[-1] == '0' or str(c)[-1] == '3' or str(c)[-1] == '6' or str(c)[-1] == '9':
        int(c)
        soma += c
    elif str(c)[-1] == '5':
        int(c)
        soma += c
    c -= 1

print(f'SOMA :  {soma}')
