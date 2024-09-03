senha = 'python123'

usuario = str(input('qual a senha: '))

while usuario != senha:
    usuario = str(input('digite a senha certa: '))

print('senha correta. Acesso permitido')