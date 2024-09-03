def financiar_carro(valor_veiculo, valor_entrada, taxa, n):
    vf = valor_veiculo - valor_entrada
    taxa = taxa / 100
    p = vf * (taxa+1) ** n * taxa
    d = (taxa + 1) ** n - 1

    v = p/d

    for i in range(48):
        v += p / d

    juros = v - vf

    cada_parcela = p/d
    print('o valor do carro é R$', valor_veiculo)
    print(f'O total a pagar é {v:,.2f}')
    print(f'A quantia de juros pagos é {juros:,.2f}')
    print(f'O total a pagar por cada parcela é {cada_parcela:,.2f}')


financiar_carro(80000, 40000, 2.9, 48)
