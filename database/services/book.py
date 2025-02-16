from database.services.generic import GenericService
from database.utils import read_sql_file


class BookService(GenericService):
    def __init__(self, conn):
        super().__init__(conn, "book")  # Chama o construtor da classe pai (GenericService) com o nome da entidade

    def get_all(self):
        """Recupera todos registro da base de dados."""
        sql_file = f"queries/read/{self.entity_name}_all.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, fetch_all=True)
