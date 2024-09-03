class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimirRaio(self):
        print('Raio: ', self.raio)

    def calculaArea(self):
        area = 3.14 * self.raio**2
        return area

    def circunferenciaCirculo(self):
        circun = 2 * 3.14 * self.raio
        return circun

circulo1 = Circulo(8)

circulo1.imprimirRaio()

area = circulo1.calculaArea()

print('AREA: ', area)

circun = circulo1.circunferenciaCirculo()

print('CIRCUNFERENCIA: ', circun)