from math import sqrt

x1 = int(input('escreva possição x¹: '))
y1 = int(input('escreva possição y¹: '))
x2 = int(input('escreva possição x²: '))
y2 = int(input('escreva possição y²: '))

d = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if d >= 10:
    print('longe da saída!')
else:
    print('perto da saída!')