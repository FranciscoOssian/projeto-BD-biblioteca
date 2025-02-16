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
        self.model = model
    
    def execute(self, sql, args):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            return self.cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            print(f"Erro {e}")
            return False

    def create(self, tuple):
        """Cria um novo registro."""
        sql_file = f"queries/create/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        self.execute(sql, tuple)
        return self.cursor.lastrowid
        
    def update(self, tuple):
        """Update um registro."""
        sql_file = f"queries/update/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, tuple)
    
    def get(self, tuple):
        """Update um registro."""
        sql_file = f"queries/read/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, tuple)

    def delete(self, tuple):
        """Delete um registro."""
        sql_file = f"queries/delete/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, tuple)