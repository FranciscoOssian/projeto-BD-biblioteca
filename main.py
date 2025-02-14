import sqlite3

from database.services import student, database, book  # Importa o módulo student do pacote services

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
        book_service = book.BookService(conn)

        # 3. Exemplos de operações CRUD (usando StudentService)

        # Cria um novo aluno
        success = student_service.create(20, "Escola Municipal")
        if success:
            print("Aluno criado com sucesso!")
            id = book_service.create('Dom Casmurro', 'Editora X', 9788594318602, 1899, 'Machado de Assis', 0, 1)
            bookData = book_service.get(id)
            if success:
                print("livro criado com sucesso!", bookData)
                #result = book_service.get()
            else:
                print("Falha ao criar livro.")
        else:
            print("Falha ao criar aluno.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # 4. Fechar a conexão com o banco de dados
        conn.close()  # Feche a conexão no bloco finally para garantir que sempre seja fechada

if __name__ == "__main__":
    main() # Chama a função main quando o script é executado