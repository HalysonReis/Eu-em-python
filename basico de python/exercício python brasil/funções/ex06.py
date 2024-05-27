

def conversao(horas):
        return horas - 12
    
def imprime_hora(horas, minutos):    
        if horas > 12:
            print(f'{conversao(horas)} : {minutos} | P.M')
        else:
            print(f'{horas} : {minutos} | A.M')

a = imprime_hora(10,3)

a