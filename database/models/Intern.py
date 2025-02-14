class Intern:
    def __init__(self, idFuncionario, fim_do_estagio):
        """
        Classe que representa um estagiário.

        """
        self.idFuncionario = idFuncionario
        self.fim_do_estagio = fim_do_estagio
    def __repr__(self):
        """Retorna uma representação string do objeto Estagiário."""
        return f"Intern(idFuncionario={self.idFuncionario}, fim_do_estagio='{self.fim_do_estagio})"
