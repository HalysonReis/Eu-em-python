terminou = True

while terminou:
    r1 = int(input('digite R1, [0 - para sair]:'))
    r2 = int(input('digite R2:'))
    if r1 == 0 or r2 == 0:
        terminou = False
    else:
        resistencia = (r1 * r2) / (r1 + r2)
        print('a resistencia é ', resistencia)
