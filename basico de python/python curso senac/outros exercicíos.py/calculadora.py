n1 = input('um numero: ')

while not(n1.isnumeric()):
    n1 = input('numero incorreto, digite um nuemro valido. \n>>>')

print('[/] divisão')
print('[+] adição')
print('[-] subtração')
print('[*] multiplicação')

operador = input('qual operação sera feita? \n>>> ')
while operador not in ['/', '+', '-', '*']:
    operador = input('operador errado. digite novemente: \n>>> ')

n2 = input('um numero: ')

while not(n2.isnumeric()):
    n2 = input('numero incorreto, digite um numero valido. \n>>>')

n1 = float(n1)
n2 = float(n2)

if operador == '/':
    resposta = n1 / n2
    
elif operador == '+':
    resposta = n1 + n2

elif operador == '-':
    resposta = n1 - n2

elif operador == '*':
    resposta = n1 * n2

print('RESPOSTA: ', resposta)