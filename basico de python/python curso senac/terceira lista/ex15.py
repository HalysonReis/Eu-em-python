n = int(input('um numero: '))
while n % 2 != 0:
    n = int(input('um numero par: '))
c = n

while c >= 0:
    if c % 2 == 0:
        print(c)
    c -= 1
