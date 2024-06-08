consumo_casa = float(input('qual o consumo da casa: '))
irradiacao_solar = float(input('qual a irradiação solar: '))
potencias_placas = float(input('potencia da placa: '))

capacidade_sistema = consumo_casa / 30 / irradiacao_solar / 0.80

wp = capacidade_sistema * 1000

qnt_placa = wp / potencias_placas

print(f'a quantidade placas necessarias para esta casa é {int(qnt_placa)} placa solares.')
