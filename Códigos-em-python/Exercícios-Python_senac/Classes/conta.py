class Conta:
    def __init__(self, nome, CPF, numero, saldo):
        self.nome = nome
        self.CPF = CPF
        self.numero = numero
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo = self.saldo - saque

    def imprimirSaldo(self):
        print('O saldo é ', self.saldo)


conta1 = Conta('halyson', 467575243, 2354, 100)

conta1.depositar(100)

conta1.sacar(150)

conta1.imprimirSaldo()