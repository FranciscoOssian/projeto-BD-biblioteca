CREATE TRIGGER IF NOT EXISTS atualizar_situacao_emprestimo
AFTER INSERT ON loan
FOR EACH ROW
BEGIN
    -- Atualiza o livro, indicando que ele está emprestado
    UPDATE book 
    SET id_loan = NEW.id
    WHERE id = NEW.id_livro;
END;
