class Pessoa:
    def __init__(self,nome,idade,endereco=' não possiu'):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def retornaNome(self):
        return self.nome
    def alterarIdade(self, nova_idade):
        self.idade = nova_idade
        print(f'nova idade: {self.idade}')
    
    def printEndereco(self):
        print(self.endereco)


pes1 = Pessoa('halyson', 18, endereco='aero racho')

print(pes1.retornaNome())
pes1.alterarIdade(44)
pes1.printEndereco()