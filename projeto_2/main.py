from livro import Livro

def main():
    # Criando dois objetos
    livro_1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
    livro_2 = Livro('Harry Potter', 'J.K. Rowling', 1997)
    
    # Testando os métodos
    print(livro_1.detalhes())
    livro_1.emprestar()
    print(livro_1.detalhes())
    livro_1.devolver()
    print(livro_1.detalhes())
    
    print(livro_2.detalhes())
    livro_2.devolver() # Não foi emprestado
    livro_2.emprestar()
    livro_2.emprestar() # Não está mais disponível
    print(livro_2.detalhes())
if __name__ == '__main__':
    main()