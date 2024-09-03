custo_de_fabrica = float(input('qual o custo de fabrica: '))

if custo_de_fabrica < 12000:
    print(f'a comisão é {custo_de_fabrica * 0.05}')
    print(f'o preço final para o consumidor é {custo_de_fabrica}')
elif custo_de_fabrica >= 12000 and custo_de_fabrica <= 25000:
    print(f'a comisão é {custo_de_fabrica * 0.1}')
    print(f'o preço final para o consumidor é {custo_de_fabrica + (custo_de_fabrica * 0.15)}')
elif custo_de_fabrica > 25000:
    print(f'a comisão é {custo_de_fabrica * 0.15}')
    print(f'o preço final para o consumidor é {custo_de_fabrica + (custo_de_fabrica * 0.20)}')