class Aluno:
    def __init__(self, nome, RA, n1, n2, n3, n4):
        self.nome = nome
        self.RA = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
    
    def mostrarSituacao(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4

        if media >= 7:
            return 'Aprovado', media
        
        elif media < 7 and media >= 5:
            return 'Exame', media
        
        elif media < 5:
            return 'Reprovado', media


aluno1 = Aluno('halyson', '986343', 3, 6, 4, 6)

situacaoAluno1 = aluno1.mostrarSituacao()

print(f'O aluno 1 está {situacaoAluno1[0]}, com a média {situacaoAluno1[1]}')