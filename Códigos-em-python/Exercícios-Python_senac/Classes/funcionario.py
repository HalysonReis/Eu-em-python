class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomeCompleto(self):
        nome = self.nome + ' ' + self.sobrenome
        print('O nome é ', nome)

    def calcularSalario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print('O salário é ', salario)

    def incrementarHoras(self, novoVH):
        self.valor_hora = self.valor_hora + novoVH


funcionario1 = Funcionario('Halyson', 'da silva', 40, 10)

funcionario1.nomeCompleto()
funcionario1.calcularSalario()
funcionario1.incrementarHoras(12)
funcionario1.calcularSalario()