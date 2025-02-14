class Library:
    def __init__(self, id, nomeBiblioteca, idFuncionario):
        """
        Classe que representa uma biblioteca.

        """
        self.id = id
        self.nomeBiblioteca = nomeBiblioteca
        self.idFuncionario  = idFuncionario

    def __repr__(self):
        """Retorna uma representação string do objeto Library."""
        return f"Library(id={self.id}, nomeBiblioteca='{self.nomeBiblioteca}', idFuncionario={self.idFuncionario})"
