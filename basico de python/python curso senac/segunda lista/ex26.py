a = float(input('um lado do triangulo: '))
b = float(input('outro lado do triangulo: '))
c = float(input('outro lado do triangulo: '))

if a == b and a == c:
    print('triangulo equilatero.')
elif a == b or a == c or b == c:
    print('triangulo isosceles.')
elif a != b and a != c:
    print('triangulo escaleno')