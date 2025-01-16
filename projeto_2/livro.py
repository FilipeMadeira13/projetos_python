class Livro:
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        
    def detalhes(self) -> str:
        """
        Mostra as informações do livro.

        Returns:
            str: Informações do livro
        """
        return (
            f'Título: {self.titulo}\n'
            f'Autor: {self.autor}\n'
            f'Ano: {self.ano}\n'
            f'Disponível: {"Sim" if self.disponivel else "Não"}'
        )
        
    def emprestar(self) -> None:
        """
        Empresta o livro se ele estiver disponível.
        """
        if self.disponivel:
            self.disponivel = False
            print(f'O livro {self.titulo} emprestado com sucesso.')
        else:
            print(f'O livro {self.titulo} não está disponível.')
            
    def devolver(self) -> None:
        """
        Resgata o livro se ele estiver emprestado.
        """
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro {self.titulo} devolvido com sucesso.')
        else:
            print(f'O livro {self.titulo} não foi emprestado.')       