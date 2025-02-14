class Employee:
    def __init__(self, nome, telefone, cargo, idFuncionario, idBiblioteca):
        
        #Classe que representa um funcionario.

        self.nome = nome
        self.telefone = telefone
        self.cargo = cargo
        self.idFuncionario = idFuncionario
        self.idBiblioteca = idBiblioteca

    def __repr__(self):
        """Retorna uma representação string do objeto Employee."""
        return f"Employee(nome={self.nome}, telefone={self.telefone}, cargo={self.cargo}, idFuncionario={self.idFuncionario}, idBiblioteca={self.idBiblioteca})"