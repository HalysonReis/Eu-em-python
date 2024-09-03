def segundos(hora, min, seg):
    segundo = seg
    segundo += hora * 60 * 60
    segundo += min * 60

    return segundo


converte = segundos(10, 30, 127)

print('em segundo fica ', converte)