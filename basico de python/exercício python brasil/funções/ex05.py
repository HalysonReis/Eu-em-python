

def somaimposto(taxa_imposto, custo):
    novo_custo = custo + (custo * taxa_imposto / 100)
    print('novo imposto', novo_custo)

somaimposto(10, 100)