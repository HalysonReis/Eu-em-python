soma = 0

for c in range(0, 1000+1):
    if str(c)[-1] == '0' or str(c)[-1] == '3' or str(c)[-1] == '6' or str(c)[-1] == '9':
        int(c)
        soma += c
    elif str(c)[-1] == '5':
        int(c)
        soma += c

print(f'SOMA :  {soma}')
