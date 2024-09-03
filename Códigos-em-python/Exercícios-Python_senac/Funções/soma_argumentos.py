def somar(*args):
    soma = 0

    for i in args:
        soma += i

    return soma


s = somar(2,3,4,6,8,5)

print(s)