def desconto(dia, **kwargs):
    if dia == 'terça-feira':
        des = kwargs['valor'] * 0.10
        contaSem = kwargs['valor'] - des
        taxa = contaSem * (kwargs['taxa'])
        conta = contaSem  + kwargs['couvert'] + taxa
    elif dia == 'quarta-feira':
        des = kwargs['valor'] * 0.15
        contaSem = kwargs['valor'] - des
        taxa = contaSem * (kwargs['taxa'])
        conta = contaSem  + kwargs['couvert'] + taxa
    elif dia == 'quinta-feira':
        des = kwargs['valor'] * 0.20
        contaSem = kwargs['valor'] - des
        taxa = contaSem * (kwargs['taxa'])
        conta = contaSem  + kwargs['couvert'] + taxa

    return conta, contaSem

conta = desconto('quarta-feira', valor=99.90, taxa=0.10, couvert=15)

print('conta sem taxa ', conta[-1])
print('conta com taxa ', conta[0])
