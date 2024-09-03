try:
    n1 = int(input('um numero: '))
    if n1 < 1:
        raise ValueError

    n2 = int(input('um numero: '))
    if n2 < 1 or n2 < n1:
        raise ValueError

    for i in range(n1, n2+1):
        c = 0
        for num in range(1, n2+1):
            if i % num == 0:
                c += 1

        if c == 2:
            print(i, ' é primo')

except ValueError:
    print('por favor digite o numero correto.')
