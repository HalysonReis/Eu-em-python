p1 = 780000 * 0.46
p2 = 780000 * 0.32
p3 = 780000 - (p1 + p2)

novo = 780000 + p1

print(f'o primeiro ganhador receberá {p1:,.2f}')
print(f'o segundo ganhador receberá {p2:,.2f}')
print(f'o terceiro ganhador receberá {p3:,.2f}')
print(f'novo premio: {novo:,.2f}')
