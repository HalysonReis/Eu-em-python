class CaixaEletronico:
    def __init__(self):
        # declarando notas
        self.nota1 = 0
        self.nota5 = 0
        self.nota10 = 0
        self.nota50 = 0
        self.nota100 = 0
        self.saque = 0

    # perguntando o valor do saque
    def saque_valor(self):
        self.saque = input('Qual valor você deseja sacar: ')
        CaixaEletronico().verifica_saque(saque=self.saque)

    # metodo para verificar o saque
    def verifica_saque(self, saque):
        # confirmando se o valor digitado é um numero
        while not (saque.isnumeric()):
            self.saque = input(
                'valor incorreto. Qual valor você deseja sacar: ')

        # confirmando se o valor está entre 10 e 600
        while int(saque) < 10 or int(saque) > 600:
            self.saque = input(
                'valor incorreto, digite um valor acima de 10 e abaixo de 600\nQual valor você deseja sacar: ')

    # metodo para verificar notas 1 e 5
    def qnt_notas_1_5(self, saque):
        saque = str(int(saque))[-1]
        if int(saque) >= 5:
            self.nota5 = 1
            self.nota1 = int(saque) - 5
        else:
            self.nota1 = int(saque)

    # metodo para verificar notas 10 e 50
    def qnt_notas_10_50(self, saque):
        saque = str(int(saque))[-2]
        if int(saque) >= 5:
            self.nota50 = 1
            self.nota10 = int(saque) - 5
        else:
            self.nota10 = int(saque)

    # metodo para verificar notas 10 e 50
    def qnt_notas_100(self, saque):
        if len(saque) == 3:
            self.nota100 = saque[0]

    # print todas notas
    def print_notas(self):
        self.saque_valor()
        self.qnt_notas_1_5(saque=self.saque)
        self.qnt_notas_10_50(saque=self.saque)
        self.qnt_notas_100(saque=self.saque)
        print(f'nota de 1: {self.nota1}\nnota de 5: {self.nota5}\nnota de 10: {
              self.nota10}\nnota de 50: {self.nota50}\nnota de 100: {self.nota100}')


CaixaEletronico().print_notas()
