placa_carro = input('o ultimo numero da placa do carro: \n>>> ')

if placa_carro.isnumeric():
    placa_carro = int(placa_carro)

if placa_carro in [0, 1]:
    print('Não Circular 2ª Feira')
elif placa_carro in [2, 3]:
    print('Não Circular 3ª Feira')
elif placa_carro in [4, 5]:
    print('Não Circular 4ª Feira')
elif placa_carro in [6, 7]:
    print('Não Circular 5ª Feira')
elif placa_carro in [8, 9]:
    print('Não Circular 6ª Feira')
else:
    print('numero invalido.')
