def calcular_tempo(tempo):
    if tempo <= 15:
        return 'não é preciso pagar pelo estacionamento'
    elif tempo % 60 != 0:
        tempo_add = 1.5 * (tempo % 60)
        horas = (tempo - (tempo % 60)) / 60
        valor_total = horas * 9 + tempo_add
    elif tempo % 60 == 0:
        valor_total = (tempo / 60) * 9
    print(f'tempo {tempo / 60} horas')
    print(f'PIS: {valor_total * 0.033}')
    print(f'CONFIS: {valor_total * 0.02}')
    print(f'ICMS: {valor_total * 0.17}')
    print(
        f'IMPOSTOS: {(valor_total * 0.033) + (valor_total * 0.02) + (valor_total * 0.17)}')
    print(f'TOTAL: {valor_total}')


calcular_tempo(248)
