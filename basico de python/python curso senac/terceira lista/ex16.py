n = int(input('um numero: '))

while n % 2 != 1:
    n = int(input('um numero impar: '))

c = 0

while c <= n:
    if c % 2 == 1:
        print(c)
    c += 1
