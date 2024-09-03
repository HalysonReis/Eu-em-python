class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalida=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalida
    
    def calcularIMC(self):
        IMC = self.peso / self.altura **2
        return IMC
    
    def obterValorMensalidade(self):
        if self.idade < 18:
            self.mensalidade = self.mensalidade - 20
            return self.mensalidade
        else: return self.mensalidade

aluno = AlunoAcademia('Halyson', 17, 70, 1.80)

IMC = aluno.calcularIMC()
print('IMC: ', IMC)

mensalidade = aluno.obterValorMensalidade()

print('MENSALIDADE: ', mensalidade)