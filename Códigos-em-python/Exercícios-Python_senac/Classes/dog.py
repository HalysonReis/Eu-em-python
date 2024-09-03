class Dog:
    def __init__(self, nome, peso, idade,cor):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.cor = cor

    def latir(self):
        print(f'{self.nome}, AU AU AU')
    
    def comer(self):
        print(f'{self.nome} comeu')


cachorro1 = Dog('bilu', 7, 5, 'caramelo')

cachorro1.latir()
cachorro1.comer()
