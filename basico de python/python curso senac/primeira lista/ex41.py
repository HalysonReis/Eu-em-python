preco = float(input('qual o valor do produto? '))

desconto = preco - (preco * 0.10)

comi_ven_des = (desconto * 0.05)

print(f'o preço do produto com desconto é {desconto}')
print(f'é necessario pagar R${comi_ven_des} ao vendedor')

parcela = preco / 3
print(f'o valor da parcela é {parcela}')

comi_ven = preco * 0.05
print(f'é necessario pagar ao vendedor R${comi_ven}')