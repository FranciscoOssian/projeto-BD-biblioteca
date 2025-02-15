class Teacher:
    def __init__(self, idLeitor, email, materia):
        """
        Classe que representa um professor.

        """
        self.idLeitor = idLeitor
        self.email = email
        self.materia = materia
        

    def __repr__(self):
        """Retorna uma representação string do objeto Teacher."""
        return f"Teacher(idLeitor={self.idLeitor}, email='{self.email}', materia={self.materia}')"
