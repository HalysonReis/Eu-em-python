class Veiculo:
    def __init__(self, marca, lugares):
        self.marca = marca
        self.lugares = lugares

    def mover(self):
        print(f'{self.marca} movimentou.')


class Moto(Veiculo):
    def __init__(self, marca, lugares):
        super().__init__(marca, lugares)
    
    def mover(self):
        print(f'{self.marca} deu GRAU.')


class Carro(Veiculo):
    def __init__(self, marca, lugares, passageiros):
        super().__init__(marca, lugares)
        self.passageiros = passageiros
    
    def getPassageiros(self):
        return self.passageiros
    
    def mover(self):
        print(f'{self.marca} fez drift.')

class Aviao(Veiculo):
    def __init__(self, marca, lugares, passageiros):
        super().__init__(marca, lugares)
        self.passageiros = passageiros
    
    def getPassageiros(self):
        return self.passageiros
    
    def mover(self):
        print(f'{self.marca} decolou.')


m1 = Moto('raley', 2)
m1.mover()

c1 = Carro('FIAT', 4, 2)
passageirosC = c1.getPassageiros()
c1.mover()

a1 = Aviao('GOL', 200, 169)
passageirosA = a1.getPassageiros()
a1.mover()