class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    
    def alterarEditora(self, nova_editora):
        self.editora = nova_editora
        
    def listarPaginas(self):
        return self.paginas


li = Livro('Minha vida', 'EU', 'Ceu', 10000)

li.alterarEditora('Deus')

print(li.editora)

paginas = li.listarPaginas()

print(paginas)