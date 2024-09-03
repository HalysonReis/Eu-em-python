km = float(input('quantos KMs rodados? >>> '))
litros = float(input('qunatos litros abastecidos? >>> '))

litro_por_km = km / litros

if litro_por_km < 8:
    print('venda o carro.')
elif litro_por_km >= 8 and litro_por_km <= 14:
    print('carro economico.')
elif litro_por_km > 14:
    print('carro super economico.')