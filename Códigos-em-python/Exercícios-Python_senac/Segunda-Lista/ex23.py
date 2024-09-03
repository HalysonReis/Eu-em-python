base_maior = int(input('qual a base miaor: '))
base_menor = int(input('qual a base menor: '))
h = int(input('qual a altura: '))

if base_maior > 0 and base_menor > 0:
    area = ((base_menor + base_maior) * h) / 2
    print(f'a area é {area}')
else:
    print('numero invalido.')