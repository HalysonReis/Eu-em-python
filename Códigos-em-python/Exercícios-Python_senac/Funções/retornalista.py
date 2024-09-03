def retornaLista(e, p):
    lista = []

    i = 0

    while i < e:
        lista.append(p)
        i += 1

    return lista

lista = retornaLista(5, 'a')

print(lista)