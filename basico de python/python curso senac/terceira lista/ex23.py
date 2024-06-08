n = int(input('um numero: '))

soma = 0

c = 0

while c < n:
    c += 1
    if c == n:
        break

    if n % c == 0:
        soma += c
        print(c)

print(soma)