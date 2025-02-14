class Book:
    def __init__(self, idLivro, titulo, editora, anoPublicacao, autor, idLivros_categorias):
        """
        Classe que representa um livro.
        """
       
        self.idLivro = idLivro
        self.titulo = titulo
        self.editora = editora
        self.anoPublicacao = anoPublicacao
        self.autor = autor
        self.idLivros_categorias = idLivros_categorias

    def __repr__(self):
        """Retorna uma representação string do objeto Book."""
        return f"Book(idLivro={self.idLivro}, titulo={self.titulo}, editora={self.editora}, ano da publicacao={self.anoPublicacao}, autor={self.autor} e idLivros_categoria={self.idLivros_categorias})"