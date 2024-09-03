class Filme:
    def __init__ (self, nome , duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print(f'O {self.nome} Começou, largue o celular e assista o filme.')
    

class FilmeAcao(Filme):
    def __init__(self, nome, duracao, duble):
        super().__init__(nome, duracao)
        self.duble = duble
    
    def explodir(self):
        print('OCORREU UMA EXPLOSSÃO.')
    
f1 = Filme('Em busca dos achados', 1.50)

f1.play()

f2 = FilmeAcao('Correndo para tras', 1.30, 'dwena jhonas')
f2.play()
f2.explodir()