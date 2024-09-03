paes = float(input('quantos pães foram vedidos? '))
broa = float(input('quntas broas foram vendidas? '))

paes = paes * 0.12
broa = broa * 1.5

soma = paes + broa

investimento = soma * 0.10

print(f'o total arrecadado foi {soma}')
print(f'deve ser investido R${investimento}')
