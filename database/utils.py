import os

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