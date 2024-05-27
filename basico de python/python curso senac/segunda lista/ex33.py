preco = float(input('qualo preço do produto? >>> '))

if preco <= 50:
    print(f'o novo preço sera {preco + (preco * 0.05)}')
elif preco > 50 and preco <= 100:
    print(f'o novo preço sera {preco + (preco * 0.10)}')
elif preco > 100:
    print(f'o novo preço sera {preco + (preco * 0.15)}')
