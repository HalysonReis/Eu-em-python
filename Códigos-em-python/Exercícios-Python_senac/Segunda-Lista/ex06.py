turno = str(input('em que turno você estuda?\n[V: vespertino; M: matutino; N: noturno] >>> ')).upper()

if turno == 'V':
    print('BOM DIA!!!!!!!')
elif turno == 'M':
    print('BOA TARDE!!!!!')
elif turno == 'N':
    print('BOA NOITE!!!!!')
else:
    print('turno invalido.')