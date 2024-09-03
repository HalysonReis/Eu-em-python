class Xadrez:
    def __init__(self):
        self.matriz = []
        self.linha = []
        self.col = {
            'h': 0,
            'g': 1,
            'f': 2,
            'e': 3,
            'd': 4,
            'c': 5,
            'b': 6,
            'a': 7
        }

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
                self.linha.append(' oT ')
                self.linha.append(' aC ')
                self.linha.append(' iB ')
                self.linha.append(' aR ')
                self.linha.append(' ER ')
                self.linha.append(' iB ')
                self.linha.append(' aC ')
                self.linha.append(' oT ')

            elif lin == 1:
                for i in range(1, 9):
                    self.linha.append(f' P{i} ')

            elif lin == 6:
                for i in range(8, 0, -1):
                    self.linha.append(f' q{i} ')

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

    def clear(self):
        print('\n'*150)

    def ler_jogada_branca(self):
        print('-='*30)
        print('Quem começa são as brancas. Suas peças estão nas linhas 7 e 8')
        print(
            'Informe as columas(col) linhas(lin) e , EX: h0 posição da Torre(To)')
        rec_peca_branca = str(
            input('Qual a posição da peça você quer movimentar: '))
        rec_jogada_branca = str(input('para onde movimentar: '))

        peca_branca = str(
            self.col[rec_peca_branca[0]]) + str(int(rec_peca_branca[1]) - 1)
        jogada_branca = str(
            self.col[rec_jogada_branca[0]]) + str(int(rec_jogada_branca[1]) - 1)

        self.movimentar_peca(peca=peca_branca, jogada=jogada_branca)

    def ler_jogada_preta(self):
        print('-='*30)
        print('Agora é a vez das pretas. Suas peças estão nas linhas 1 e 2')
        print(
            'Informe as linhas(lin) e columas(col), EX: h0 posição da Torre(To)')
        rec_peca_preta = str(
            input('Qual a posição da peça você quer movimentar: '))
        rec_jogada_preta = str(input('para onde movimentar: '))

        peca_preta = str(
            self.col[rec_peca_preta[0]]) + str(int(rec_peca_preta[1]) - 1)
        jogada_preta = str(
            self.col[rec_jogada_preta[0]]) + str(int(rec_jogada_preta[1]) - 1)

        self.movimentar_peca(peca=peca_preta, jogada=jogada_preta)

    def movimentar_peca(self, peca, jogada):
        self.matriz[int(jogada[1])][int(jogada[0])
                                    ] = self.matriz[int(peca[1])][int(peca[0])]
        self.matriz[int(peca[1])][int(peca[0])] = ' __ '


xadrez = Xadrez()

xadrez.gerar_tabuleiro()

while True:
    xadrez.print_tebuleiro()
    xadrez.ler_jogada_branca()
    xadrez.print_tebuleiro()
    xadrez.ler_jogada_preta()
    xadrez.clear()
