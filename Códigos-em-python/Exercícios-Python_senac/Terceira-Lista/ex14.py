c = 0 
n = int(input('um numero: '))
while n % 2 != 0:
    n = int(input('um numero par: '))

while c <= n:
    if c % 2 == 0:
        print(c)
    c += 1