CREATE TRIGGER loan_insert_trigger
AFTER INSERT ON loan
BEGIN
    -- Atualiza o livro, indicando que ele está emprestado
    UPDATE book 
    SET id_loan = NEW.id
    WHERE id = NEW.id_livro;
END;
