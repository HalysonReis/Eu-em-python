class Triangulo:
    def __init__(self, LA, LB, LC):
        self.LA = LA
        self.LB = LB
        self.LC = LC
    
    def calcularPerimetro(self):
        perimetro = self.LA + self.LB + self.LC
        return perimetro
    
    def getMaiorLado(self):
        lados = [self.LA , self.LB, self.LC]

        maior = 0

        for i in lados:
            if i > maior:
                maior = i
        
        return maior

triangulo1 = Triangulo(2,3,4)

perimetro = triangulo1.calcularPerimetro()
maioLado = triangulo1.getMaiorLado()

print('PERIMETRO: ', perimetro)
print('MAIOR LADO: ', maioLado)