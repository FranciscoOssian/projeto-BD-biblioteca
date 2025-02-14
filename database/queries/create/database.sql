CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    age INTEGER,
    school TEXT
);
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY NOT NULL,
    titulo TEXT NOT NULL,
    editora TEXT,
    isbn INTEGER,
    ano_publicacao INTEGER,
    autor TEXT,
    id_emprestimo INTEGER,
    id_categoria INTEGER ,
);
CREATE TABLE IF NOT EXISTS intern (
    id INTEGER PRIMARY KEY,
    fim_estagio TIMESTAMP, 
);
CREATE TABLE IF NOT EXISTS librarian (
    id INTEGER PRIMARY KEY,
    tempo_trabalhado TIMESTAMP,
);
CREATE TABLE IF NOT EXISTS reader (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    data_registro TIMESTAMP NOT NULL,
    tipo_leitor TEXT
);
CREATE TABLE IF NOT EXISTS teacher (
    id INTEGER PRIMARY KEY NOT NULL,
    email TEXT NOT NULL,
    materia TEXT
);
CREATE TABLE IF NOT EXISTS emprestimo (
    id INTEGER PRIMARY KEY,
    data_retirado TIMESTAMP NOT NULL,
    data_devolucao TIMESTAMP NOT NULL,
    id_livro INTEGER NOT NULL,
    id_leitor INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS categorias_livro (
    isbn INTEGER NOT NULL,
    id_livro INTEGER NOT NULL,
    id_categoria PRIMARY KEY INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    ranking INTEGER,
);
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    id_funcionario INTEGER
);
