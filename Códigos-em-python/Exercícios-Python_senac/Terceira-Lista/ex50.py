n = int(input('digite um numero: '))

i = int(input('o numero para dividir:'))
j = int(input('mais um numero para dividir:'))

for num in range(1, n):
    if i % num == 0:
        print(num)
    elif j % num == 0:
        print(num)