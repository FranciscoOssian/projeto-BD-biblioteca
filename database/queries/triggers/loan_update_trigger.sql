CREATE TRIGGER loan_update_trigger
AFTER UPDATE OF data_retirado ON loan
BEGIN
    UPDATE book
    SET id_loan = NULL
    WHERE id = NEW.id_livro;  -- A condição WHERE é necessária
END;