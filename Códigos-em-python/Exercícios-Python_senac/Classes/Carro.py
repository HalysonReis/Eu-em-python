class Carro:
    def __init__ (self, modelo, marca, cor, ano, valor, consumo, nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel

    def ligar(self, ligarCarro=0):
        ligarCarro = ligarCarro
        if ligarCarro == 0:
            print('O carro está desligado, necessario ligar o carro.')
        
        elif ligarCarro == 1:
            print('o carro está ligado.')


    def abastecer(self, novo_nivel):
        self.nivel = novo_nivel
    
    def andar(self, KM):
        return KM
    
    def verifica_nivel(self, KM):
        liPKM = KM * self.consumo
        print(f'Gastou {liPKM} listros.')
    

    def imposto(self):
        pagarImposto = self.valor * 1.25
        print(f'deve pagar R${pagarImposto} de imposto')

c1 = Carro('gol', 'fiat', 'vermelho', 1999, 20000, 7)
c1.ligar(1)
c1.abastecer(50)
print('O nivel: ', c1.nivel)
Kms = c1.andar(70)
c1.verifica_nivel(Kms)
c1.imposto()
