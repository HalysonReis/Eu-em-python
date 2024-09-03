latas = float(input('quantas latas foram compradas? '))
garrafa_p = float(input('quantas garrafas pequenas? '))
garrafa_g = float(input('quantas garrafas grandes? '))
latas = latas * 350
garrafa_p = garrafa_p * 600

litros = ((latas + garrafa_p) / 1000) + garrafa_g

print(f'foram comprados {litros} litros')