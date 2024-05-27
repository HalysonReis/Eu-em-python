print('-'*36)
print('-=-=-=-=-=-= BEM VINDO! -=-=-=-=-=-=\n')
nome = str(input('Qual seu nome? ')).capitalize()
print(f'\nMuito bem {nome}, estas são as opções.\n')

lista_produtos = []
lista_codigo_produto = []
lista_descricão_produto = []
lista_qnt_estoque = []

while True:
    print('-'*30)
    print('[0]: para ver lista de produto.')
    print('[1]: para adicionar produto.')
    print('[2]: remover produto.')
    print('[3]: editar produto.')
    print('[4]: para sair.')
    print('-'*30)
    acao_usuario = int(input(f'O que deseja fazer, {nome}? --> '))

    if acao_usuario == 4:
        print('\nEncerrando o programa.\n')
        break

    elif acao_usuario == 0:
        if len(lista_produtos) == 0:
            print(f'\nSinto muito {nome}, mas a lista de produtos esta vazia.\n')
        else:
            print(f'\nEstá aqui a lista {nome}.\n')
            for i, produto in enumerate(lista_produtos):
                print('-=' * 30)
                print(f'produto {i+1}°: {lista_produtos[i]}')
                print(f'produto {i+1}°: {lista_codigo_produto[i]}')
                print(f'produto {i+1}°: {lista_descricão_produto[i]}')
                print(f'produto {i+1}°: {lista_qnt_estoque[i]}')
                

    elif acao_usuario == 1:
        print('\n')
        print('-='*30)
        produto = str(input('adicione um produto: --> '))
        codigo_produto = str(input('Qual é o codigo do produto: --> '))
        descricão_produto = str(input('qual é a descrição do produto: --> '))
        qnt_estoque = int(input('qual a quantidade do produto no estoque: --> '))

        print('\n----- confirme se está correto -----')
        print(f'produto: {produto}')
        print(f'codigo do produto: {codigo_produto}')
        print(f'descrição do produto: {descricão_produto}')
        print(f'quantidade em estoque: {qnt_estoque}')
        adicionar = str(input(f'{nome}, você deseja adicionar esse produto? --> ')).lower()

        if adicionar[0] == 's':
            lista_produtos.append(produto)
            lista_codigo_produto.append(codigo_produto)
            lista_descricão_produto.append(descricão_produto)
            lista_qnt_estoque.append(qnt_estoque)
            print('\nProduto adicionado com sucesso')
        else:
            continue
    
    elif acao_usuario == 2:
        if len(lista_produtos) == 0:
            print(f'\nSinto muito {nome}, mas a lista de produtos esta vazia.\n')
        else:
            print('-='*30)
            for i in lista_produtos:
                print(f'\nProduto {lista_produtos.index(i) + 1}°: {i}')
            
            print('\n')
            print('-='*30)
            retirar_produto = str(input(f'{nome}, qual item você quer remover? --> '))
            if retirar_produto not in lista_produtos:
                print('\nAlgo está errado o item não existe.\n')
                editar_item = str(input(f'{nome}, qual item você quer remover? --> '))

            lista_produtos.remove(retirar_produto)
            
            print('\nItem removido.')
            for i in lista_produtos:
                print(f'\nProduto {lista_produtos.index(i) + 1}°: {i}')


    elif acao_usuario == 3:
        if len(lista_produtos) == 0:
            print(f'\nSinto muito {nome}, mas a lista de produtos esta vazia.\n')
        else:
            print('-='*30, '\n')
            for i in lista_produtos:
                print(f'produto {lista_produtos.index(i) + 1}°: {i}\n')

            editar_item = str(input(f'{nome}, qual item você quer editar? --> '))

            if editar_item not in lista_produtos:
                print('\nAlgo está errado o item não existe.\n')
                editar_item = str(input(f'{nome}, qual item você quer editar? --> '))
            i_item = lista_produtos.index(editar_item)

            print('\n')
            print('-'*30)
            print('[0]: para trocar o produto.')
            print('[1]: para trocar o codigo do produto.')
            print('[2]: para trocar a descrição do  produto.')
            print('[3]: para alterar a quantidade no estoque.')
            print('[4] para sair.')
            print('-'*30)
            escolha_usuario = int(input(f'{nome}, qual você deseja alterar? --> '))

            match escolha_usuario:
                case 0:
                    lista_produtos[i_item] = str(input('\nEDITE: --> '))
                case 1:
                    lista_codigo_produto[i_item] = str(input('\nEDITE: --> '))
                case 2:
                    lista_descricão_produto[i_item] = str(input('\nEDITE: --> '))
                case 3:
                    lista_qnt_estoque[i_item] = str(input('\nEDITE: --> '))
                case 4:
                    continue
                case _:
                    print('OPÇÃO INVALIDA!!!!!')
    else:
        print('OPÇÃO INVALIDA!!!')


print(f'Obrigado {nome}, volte sempre.')