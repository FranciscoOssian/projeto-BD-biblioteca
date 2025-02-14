from database.utils import read_sql_file

class GenericService:
    def __init__(self, conn, entity_name, model=None):
        """
        Classe base para serviços CRUD genéricos.

        Args:
            conn: A conexão com o banco de dados.
            entity_name: O nome da entidade (ex: "aluno", "livro").
        """
        self.conn = conn
        self.cursor = conn.cursor()
        self.entity_name = entity_name

    def create(self, *args):
        """Cria um novo registro."""
        sql_file = f"queries/create/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao criar {self.entity_name}: {e}")
            return False

    def get(self, id_value):
        """Busca um registro pelo ID."""
        sql_file = f"queries/read/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        try:
            self.cursor.execute(sql, (id_value,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"Erro ao buscar {self.entity_name} com id {id_value}: {e}")
            return None

    def update(self, id_value, *args):
        """Atualiza um registro."""
        sql_file = f"queries/update/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        try:
            self.cursor.execute(sql, (*args, id_value))  # Assume ID é o último parâmetro
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao atualizar {self.entity_name}: {e}")
            return False

    def delete(self, *id_value):
        """Deleta um registro."""
        sql_file = f"queries/delete/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        try:
            self.cursor.execute(sql, id_value)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao deletar {self.entity_name}: {e}")
            return False
        