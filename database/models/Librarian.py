class Student:
    def __init__(self, idFuncionario, anosTrabalhados):
        """
        Classe que representa um bibliotecario.

        """
        self.idFuncionario = idFuncionario
        self.anosTrabalhados = anosTrabalhados
    def __repr__(self):
        """Retorna uma representação string do objeto Librarian."""
        return f"Librarian(idFuncionario={self.idFuncionario}, anosTrabalhados='{self.anosTrabalhados})"
