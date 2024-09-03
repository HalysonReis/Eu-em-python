valor_venda = float(input('qual o valor da venda: '))

if valor_venda >= 100000:
    print(f'a comisão sera de {700 + (valor_venda * 0.16)}')
elif valor_venda < 100000 and valor_venda >= 80000:
    print(f'a comisão sera de {650 + (valor_venda * 0.14)}')
elif valor_venda < 80000 and valor_venda >= 60000:
    print(f'a comisão sera de {600 + (valor_venda * 0.14)}')
elif valor_venda < 600000 and valor_venda >= 40000:
    print(f'a comisão sera de {500 + (valor_venda * 0.14)}')
elif valor_venda < 40000 and valor_venda >= 20000:
    print(f'a comisão sera de {450 + (valor_venda * 0.14)}')
elif valor_venda < 20000:
    print(f'a comisão sera de {400 + (valor_venda * 0.14)}')
