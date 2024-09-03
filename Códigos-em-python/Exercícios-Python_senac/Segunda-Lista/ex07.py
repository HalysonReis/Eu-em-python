produto = float(input('qual o preço de aquisição: '))

if produto < 50:
    acrescimo = produto + (produto * 0.45)
    print(f'o produto de R${produto} deve ser vendido por R${acrescimo}')
else:
    acrescimo = produto + (produto * 0.30)
    print(f'o produto de R${produto} deve ser vendido por R${acrescimo}')
