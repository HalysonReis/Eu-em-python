def soma_imposto(preco, taxa):
    novo_preco = preco + (preco * (taxa / 100))
    return novo_preco

produto = soma_imposto(preco= 100, taxa= 20)

print('o preço do pruduto com imposto fica: ', produto)