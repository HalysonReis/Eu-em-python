altura = float(input('qual a sua altura? '))
sexo = str(input('qual seu sexo? ')).upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'o seu peso ideal é {peso_ideal:.2f}')
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 58
    print(f'o seu peso ideal é {peso_ideal:.2f}')