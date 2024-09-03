def media(*args):
    soma = 0

    for i in args:
        soma += i

    m = soma / len(args)
    return m


m = media(7,7,7,7,7,7,7)

print(m)