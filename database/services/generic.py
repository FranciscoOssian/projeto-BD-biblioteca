from typing import List
from database.utils import read_sql_file

class GenericService:
    def __init__(self, conn, entity_name, model=None):
        """
        Classe base para serviços CRUD genéricos.

        Args:
            conn: A conexão com o banco de dados.
            entity_name: O nome da entidade (ex: "aluno", "livro").
            model: Opcional, um modelo para mapear os resultados.
        """
        self.conn = conn
        self.cursor = conn.cursor()
        self.entity_name = entity_name
        self.model = model
    
    def execute(self, sql, params=None, fetch_one=False, fetch_all=False, many=False):
        """Executa uma query SQL segura."""
        try:
            if many:
                self.cursor.executemany(sql, params or [()])
            else:
                self.cursor.execute(sql, params or ())
            self.conn.commit()

            if fetch_one:
                return self.cursor.fetchone()
            elif fetch_all:
                return self.cursor.fetchall()
            else:
                return True  # Para operações como INSERT, UPDATE e DELETE

        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao executar SQL: {e}")
            return False
    
    def create_many(self, data_list: List[tuple]):
        """Cria vários registros e retorna os IDs inseridos"""
        sql_file = f"queries/create/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        self.execute(sql, data_list, many=True)
        return True

    def create(self, data_tuple):
        """Cria um novo registro e retorna o ID inserido."""
        sql_file = f"queries/create/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        success = self.execute(sql, data_tuple)
        return self.cursor.lastrowid if success else None
        
    def update(self, data_tuple):
        """Atualiza um registro existente."""
        sql_file = f"queries/update/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, data_tuple)

    def get(self, id):
        """Recupera um registro da base de dados."""
        sql_file = f"queries/read/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, (id,), fetch_one=True)


    def delete(self, data_tuple):
        """Deleta um registro."""
        sql_file = f"queries/delete/{self.entity_name}.sql"
        sql = read_sql_file(sql_file)
        return self.execute(sql, data_tuple)
