import sqlite3
from database.services import student, database, book  # Importa os módulos necessários

def main():
    """Função principal para demonstrar o uso da biblioteca."""
    
    # 1. Configurar a conexão com o banco de dados
    conn = sqlite3.connect("app.db")
    if conn is None:
        print("Erro ao conectar ao banco de dados. Verifique a configuração.")
        return

    try:
        # 2. Criar objetos de serviço
        db_service = database.DataBaseService(conn)
        db_service.create()
        student_service = student.StudentService(conn)
        book_service = book.BookService(conn)
        
        # 3. Operação: Criar aluno
        success = student_service.create(20, "Escola Municipal")
        if success:
            print("Aluno criado com sucesso!")
        else:
            print("Falha ao criar aluno.")

        # 4. Operação: Deletar um aluno
        delete_success = student_service.delete(2)
        if delete_success:
            print("Aluno deletado com sucesso!")
        else:
            print("Falha ao deletar aluno.")

        # 3. Operação: Criar um novo aluno
        create_success = student_service.create(19, "Escola Do Bairro")
        if create_success:
            print("Aluno criado com sucesso!")
            
            # 5. Operação: Criar um livro
            book_id = book_service.create('Dom Casmurro', 'Editora X', 9788594318602, 1899, 'Machado de Assis', 0, 1)
            book_data = book_service.get(book_id)
            if book_data:
                print("Livro criado com sucesso!", book_data)
            else:
                print("Falha ao criar livro.")
        else:
            print("Falha ao criar aluno.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # 6. Fechar a conexão com o banco de dados
        conn.close()

if __name__ == "__main__":
    main()
