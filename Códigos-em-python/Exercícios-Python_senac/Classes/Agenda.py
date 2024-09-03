class Agenda:
    def __init__(self, dia, mes, ano , anotacoes = []):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacoes = anotacoes

    def validarData(self):
        if self.dia > 0 and self.dia < 32:
            if self.mes > 0 and self.mes < 13:
                 pass
            else: self.mes = int(input('digite o mes certo: '))
        else: self.dia = int(input('digite o dia certo: '))

    def anotarTarrefa(self, anotacao):
        self.anotacoes.append(anotacao)

    def mostrarAnotacoes(self):
        for i in self.anotacoes:
            print(i)


agenda1 = Agenda(0, 13, 2014)

data = agenda1.validarData()

agenda1.anotarTarrefa('Hoje eu...')
agenda1.anotarTarrefa('Hoje eu...')
agenda1.anotarTarrefa('Hoje eu...')
agenda1.anotarTarrefa('Hoje eu...')
agenda1.anotarTarrefa('Hoje eu...')

agenda1.mostrarAnotacoes()

