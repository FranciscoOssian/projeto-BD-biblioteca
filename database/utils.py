import os
import sqlite3

def read_sql_file(filepath):
    """
    Lê um arquivo SQL e retorna a consulta SQL.

    Args:
        filepath: O caminho para o arquivo SQL.

    Returns:
        A consulta SQL como uma string.
    """
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database/", filepath)
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo SQL '{filepath}' não encontrado.")

def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data

def get_db():
    conn = sqlite3.connect("app.db")
    conn.row_factory = row_to_dict
    if conn is None:
        print("Erro ao conectar ao banco de dados. Verifique a configuração.")
        return
    return conn