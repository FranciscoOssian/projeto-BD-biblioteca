class Reader:
    def __init__(self, idLeitor, nome, endereco, dataRegistro, tipoLeitor):
        """
        Classe que representa um leitor.

        """
        self.idLeitor = idLeitor
        self.nome = nome
        self.endereco = endereco
        self.dataRegistro = dataRegistro
        self.tipoLeitor = tipoLeitor

    def __repr__(self):
        """Retorna uma representação string do objeto Reader."""
        return f"Reader(idLeitor={self.idLeitor}, nome='{self.nome}', endereço={self.endereco}, dataRegistro='{self.dataRegistro}, tipoLeitor = {self.tipoLeitor}')"
