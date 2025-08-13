
from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo

class Biblioteca: 
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, id_livro):
        self.livros = [livro for livro in self.livro if livro.id_livro != id_livro]
    
    def emprestar_livro(self, id, id_livro):
        usuario = None 
        for u in self.usuarios:
            if u.id == id:
                usuario = u 
                break
        livro = None
        for l in self.livros:
            if l.id_livro == id_livro and l.disponivel == True:
                livro = l 
                break 
        
        if usuario and livro: 
            livro.disponivel = False
            emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(emprestimo)
            print(f"O livro {livro.titulo} foi emprestado para {usuario.nome}")
        else:
            print('O livro não esta disponível ou usuário não encontrado')

    def devolver_livro(self, id_livro):
        for e in self.emprestimos:
            if e.livro.id_livro == id_livro:
                e.livro.disponivel = True
                print(f'O livro {e.livro.titulo} devolvido com sucesso')
                break
            print('Livro não encontrado nos empréstimos')