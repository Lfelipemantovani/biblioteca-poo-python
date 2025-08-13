from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

biblio = Biblioteca()

biblio.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", "123", '1955'))
biblio.adicionar_livro(Livro("1984", "George Orwell", "456", '1992'))
biblio.adicionar_livro(Livro("A Metamorfose", "Franz Kafka", "223", "1915"))
biblio.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "334", "1954"))
biblio.adicionar_livro(Livro("Crime e Castigo", "Fiódor Dostoiévski", "445", "1866"))
biblio.adicionar_livro(Livro("Ulisses", "James Joyce", "556", "1922"))
biblio.adicionar_livro(Livro("Moby Dick", "Herman Melville", "667", "1851"))
biblio.adicionar_livro(Livro("A Revolução dos Bichos", "George Orwell", "778", "1945"))
biblio.adicionar_livro(Livro("Grande Sertão: Veredas", "João Guimarães Rosa", "889", "1956"))
biblio.adicionar_livro(Livro("O Nome da Rosa", "Umberto Eco", "990", "1980"))
biblio.adicionar_livro(Livro("O Sol é para Todos", "Harper Lee", "001", "1960"))
biblio.adicionar_livro(Livro("Viagem ao Centro da Terra", "Júlio Verne", "112", "1864"))

biblio.adicionar_usuario(Usuario("Carlos", 3))
biblio.adicionar_usuario(Usuario("Diana", 4))
biblio.adicionar_usuario(Usuario("Eduardo", 5))
biblio.adicionar_usuario(Usuario("Fernanda", 6))
biblio.adicionar_usuario(Usuario("Gustavo", 7))
biblio.adicionar_usuario(Usuario("Helena", 8))
biblio.adicionar_usuario(Usuario("Igor", 9))
biblio.adicionar_usuario(Usuario("Julia", 10))
biblio.adicionar_usuario(Usuario("Kleber", 11))
biblio.adicionar_usuario(Usuario("Laura", 12))

biblio.emprestar_livro(1, '123')
biblio.emprestar_livro(4, '223')

biblio.devolver_livro('223')

biblio.emprestar_livro(9, '223')
