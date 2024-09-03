def tabela_produto():
    print('-=- tabela de produtos -=-')
    soma = 1.99
    for item in range(1, 51):
        print(f'{item} - {soma}')
        soma += 1.99

tabela_produto()
