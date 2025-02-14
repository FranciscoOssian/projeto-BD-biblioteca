import sqlite3

from database.services import student, database  # Importa o módulo student do pacote services

def main():
    """Função principal para demonstrar o uso da biblioteca."""
    
    # 1. Configurar a conexão com o banco de dados
    
    conn = sqlite3.connect("app.db")

    if conn is None:
        print("Erro ao conectar ao banco de dados. Verifique a configuração.")
        return

    try:
        # 2. Criar um objeto StudentService
        db_service = database.DataBaseService(conn)
        db_service.create()
        student_service = student.StudentService(conn)  # Cria uma instância de StudentService

        # 3. Exemplos de operações CRUD (usando StudentService)
        """
        # Cria um novo aluno
        success = student_service.delete(2)
        if success:
            print("Aluno Deletado com sucesso!")
        else:
            print("Falha ao Deletar aluno.")
        """
        


    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # 4. Fechar a conexão com o banco de dados
        conn.close()  # Feche a conexão no bloco finally para garantir que sempre seja fechada

if __name__ == "__main__":
    main() # Chama a função main quando o script é executado
