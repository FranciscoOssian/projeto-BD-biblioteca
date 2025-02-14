class Loan:
    def __init__(self, id, data_retirado, data_dev_prevista, isbn_livro, id_livro, id_leitor):
        """
        Classe que representa um empréstimo.
        """
        self.id = id
        self.data_retirado = data_retirado
        self.data_dev_prevista = data_dev_prevista
        self.isbn_livro = isbn_livro
        self.id_livro = id_livro
        self.id_leitor = id_leitor
        

    def __repr__(self):
        """Retorna uma representação string do objeto Emprestimo."""
        return (f"Emprestimo(id={self.id}, data_retirado='{self.data_retirado}', "
                f"data_dev_prevista='{self.data_dev_prevista}', isbn_livro={self.isbn_livro}, "
                f"id_livro={self.id_livro}, id_leitor={self.id_leitor})")
