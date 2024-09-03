class Pessoa:
    def __init__(self, matricula, idade, nome):
        self.matricula = matricula
        self.idade = idade
        self.nome = nome
    

class Aluno(Pessoa):
    def __init__(self, matricula, idade, nome, media, *notas):
        super().__init__(matricula, idade, nome)
        self.notas = notas
        self.media = media

    def getNotas(self):
        return self.notas
    
    def getMedia(self):
        return self.media
    
a1 = Aluno(35456, 18, 'Halyson', 10, 10, 8, 9, 10)
a1N = a1.getNotas()
print(a1N)
a1M = a1.getMedia()
print(a1M)

class Professor(Pessoa):
    def __init__(self, matricula, idade, nome, formacao, disciplina, cargaHoraria, salario):
        super().__init__(matricula, idade, nome)
        self.formacao = formacao
        self.discipina = disciplina
        self.cargaHoraria = cargaHoraria
        self.salario = salario
    
    def lecionar(self):
        print(f'{self.nome} está lecionando')
    
    def calcularMedia(self, *notas):
        soma = 0
        for i in notas:
            soma += i
        media = soma / len(notas)

        return media

p1 = Professor(34635, 38, 'Thiago', 'Engenharia', 'python', 200, 10000)
p1.lecionar()
calculoMedia = p1.calcularMedia(10,8,9,10)
print(calculoMedia)