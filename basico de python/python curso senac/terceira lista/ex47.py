soma = 0
quad = 0

for i in range(1, 101):
    soma += i ** 2
    quad += i

quad = quad ** 2

diferenca = quad - soma

print(soma)
print(quad)
print(diferenca)