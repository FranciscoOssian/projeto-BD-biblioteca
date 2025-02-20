CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    school TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES reader(id)
);

CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY NOT NULL,
    titulo TEXT NOT NULL,
    editora TEXT,
    isbn TEXT,
    ano_publicacao INTEGER,
    autor TEXT,
    id_loan INTEGER NULL,
    id_categoria INTEGER NULL,
    FOREIGN KEY (id_loan) REFERENCES loan(id),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS intern (
    id INTEGER PRIMARY KEY,
    fim_estagio TIMESTAMP,
    FOREIGN KEY (id) REFERENCES employee(id)
);

CREATE TABLE IF NOT EXISTS librarian (
    id INTEGER PRIMARY KEY,
    tempo_trabalhado TIMESTAMP,
    FOREIGN KEY (id) REFERENCES employee(id)
);

CREATE TABLE if NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL
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
    materia TEXT,
    FOREIGN KEY (id) REFERENCES reader(id)
);

CREATE TABLE IF NOT EXISTS loan (
    id INTEGER PRIMARY KEY,
    data_retirado TIMESTAMP NULL,
    data_devolucao TIMESTAMP NOT NULL,
    id_livro INTEGER NOT NULL,
    id_leitor INTEGER NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES book(id)
    FOREIGN KEY (id_leitor) REFERENCES reader(id)
);

CREATE TABLE IF NOT EXISTS categorias_livro (
    isbn INTEGER NOT NULL,
    id_livro INTEGER NOT NULL,
    id_categoria INTEGER PRIMARY KEY NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    ranking INTEGER
);

CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL
);
