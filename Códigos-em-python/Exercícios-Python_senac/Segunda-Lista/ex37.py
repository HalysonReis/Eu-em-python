peso = float(input('qual o seu peso: >>> '))
altura = float(input('qual a sua altura: >>> '))

imc = peso / (altura ** 2)
print(f'seu IMc é {imc}')

if imc < 18.5:
    print('abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('saúdavel.')
elif imc >= 25 and imc < 30:
    print('peso em excesso.')
elif imc >= 30 and imc < 35:
    print('obesidade grau I.')
elif imc >= 35 and imc < 40:
    print('obesidade grau II')
elif imc >= 40:
    print('obesidade grau II')