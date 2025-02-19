INSERT INTO book (titulo, editora, isbn, ano_publicacao, autor, id_loan) 
VALUES (?, ?, ?, ?, ?, ?) RETURNING id;