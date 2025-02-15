from database.services.generic import GenericService
from database.utils import read_sql_file

class DataBaseService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "database") 
        
    def create(self):
        """Cria um novo registro."""
        sql_file = f"queries/create/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        try:
            self.cursor.executescript(sql)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao criar {self.entity_name}: {e}")
            return False