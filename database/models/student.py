class Student:
    def __init__(self, idLeitor, nome, idade, escola):
        """
        Classe que representa um aluno.

        Args:
            idLeitor: O ID do aluno (chave primária).
            nome: O nome do aluno.
            idade: A idade do aluno.
            escola: A escola do aluno.
        """
        self.idLeitor = idLeitor
        self.nome = nome
        self.idade = idade
        self.escola = escola

    def __repr__(self):
        """Retorna uma representação string do objeto Student."""
        return f"Student(idLeitor={self.idLeitor}, nome='{self.nome}', idade={self.idade}, escola='{self.escola}')"