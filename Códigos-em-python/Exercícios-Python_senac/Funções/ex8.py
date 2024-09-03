def pescador(peixe):
    if peixe > 50:
        kilo_excedido = peixe - 50
        multa = kilo_excedido * 4

    print(f'foram excedidos {kilo_excedido} Kgs')
    print(f'é preciso pagar um total de {multa} de multa')

pescador(peixe=55)