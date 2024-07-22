import time


class Xadrez:
    def __init__(self):
        self.matriz = []
        self.linha = []

    def gerar_tabuleiro(self):
        for lin in range(0, 8):
            self.linha = []
            if lin == 0:
                self.linha.append(' To ')
                self.linha.append(' Ca ')
                self.linha.append(' Bi ')
                self.linha.append(' RE ')
                self.linha.append(' Ra ')
                self.linha.append(' Bi ')
                self.linha.append(' Ca ')
                self.linha.append(' To ')

            elif lin == 7:
                self.linha.append(' To ')
                self.linha.append(' Ca ')
                self.linha.append(' Bi ')
                self.linha.append(' Ra ')
                self.linha.append(' RE ')
                self.linha.append(' Bi ')
                self.linha.append(' Ca ')
                self.linha.append(' To ')

            elif lin == 1:
                for i in range(1, 9):
                    self.linha.append(f' P{i} ')

            elif lin == 6:
                for i in range(8, 0, -1):
                    self.linha.append(f' P{i} ')

            else:
                for col in range(0, 8):
                    self.linha.append(' __ ')

            self.matriz.append(self.linha)

    def print_tebuleiro(self):
        x = 1
        print('Col | h | g | f | e | d | c | b | a')
        print('Lin   |   |   |   |   |   |   |   |')
        for lin in self.matriz:
            print(x, end=' -- ')
            for col in lin:
                print(col, end=(''))
            print(end=('\n'))
            x += 1


xadrez = Xadrez()


xadrez.gerar_tabuleiro()
xadrez.print_tebuleiro()
