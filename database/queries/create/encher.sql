-- Inserindo dados na tabela employee
INSERT INTO employee (id, nome, telefone, id_library) VALUES
(1, 'Carlos Silva', '11987654321', 1),
(2, 'Ana Souza', '11976543210', 1),
(3, 'Bruno Lima', '11965432178', 1),
(4, 'Fernanda Alves', '11954321678', 1),
(5, 'Lucas Rocha', '11943216789', 1),
(6, 'Juliana Mendes', '11932167890', 1),
(7, 'Roberto Nunes', '11921098765', 1),
(8, 'Patrícia Gomes', '11910987654', 1),
(9, 'Tiago Fernandes', '11909876543', 1),
(10, 'Mariana Costa', '11908765432', 1);

-- Inserindo dados na tabela student
INSERT INTO student (id, age, school) VALUES
(1, 15, 'Escola Estadual A'),
(2, 16, 'Escola Estadual B'),
(3, 14, 'Escola Estadual C'),
(4, 17, 'Escola Municipal D'),
(5, 15, 'Escola Municipal E'),
(6, 16, 'Colégio Técnico F'),
(7, 14, 'Colégio Militar G'),
(8, 17, 'Escola Particular H'),
(9, 15, 'Colégio Estadual I'),
(10, 16, 'Escola Internacional J');

-- Inserindo dados na tabela intern
INSERT INTO intern (id, fim_estagio) VALUES
(1, '2025-06-30 00:00:00'),
(2, '2025-12-31 00:00:00'),
(3, '2026-03-15 00:00:00'),
(4, '2026-09-10 00:00:00'),
(5, '2025-11-20 00:00:00'),
(6, '2025-08-05 00:00:00'),
(7, '2026-07-25 00:00:00'),
(8, '2025-10-30 00:00:00'),
(9, '2026-04-14 00:00:00'),
(10, '2026-12-20 00:00:00');

-- Inserindo dados na tabela librarian
INSERT INTO librarian (id, tempo_trabalhado) VALUES
(1, '2020-01-01 00:00:00'),
(2, '2018-05-15 00:00:00'),
(3, '2019-07-20 00:00:00'),
(4, '2017-02-10 00:00:00'),
(5, '2021-09-30 00:00:00'),
(6, '2016-11-05 00:00:00'),
(7, '2022-04-18 00:00:00'),
(8, '2023-06-12 00:00:00'),
(9, '2015-08-25 00:00:00'),
(10, '2014-03-14 00:00:00');

-- Inserindo dados na tabela reader
INSERT INTO reader (id, nome, endereco, data_registro, tipo_leitor) VALUES
(1, 'João Pereira', 'Rua A, 123', '2023-01-10 10:00:00', 'Aluno'),
(2, 'Maria Fernandes', 'Rua B, 456', '2023-02-15 11:30:00', 'Professor'),
(3, 'Carlos Mendes', 'Rua C, 789', '2023-03-20 09:15:00', 'Pesquisador'),
(4, 'Fernanda Costa', 'Rua D, 101', '2023-04-05 14:45:00', 'Aluno'),
(5, 'Tiago Oliveira', 'Rua E, 112', '2023-05-22 16:20:00', 'Professor'),
(6, 'Juliana Rocha', 'Rua F, 214', '2023-06-30 08:50:00', 'Aluno'),
(7, 'Bruno Nunes', 'Rua G, 315', '2023-07-18 13:10:00', 'Pesquisador'),
(8, 'Mariana Lima', 'Rua H, 416', '2023-08-21 11:55:00', 'Professor'),
(9, 'Lucas Almeida', 'Rua I, 517', '2023-09-12 10:05:00', 'Aluno'),
(10, 'Patrícia Silva', 'Rua J, 618', '2023-10-25 15:30:00', 'Pesquisador');

-- Inserindo dados na tabela teacher
INSERT INTO teacher (id, email, materia) VALUES
(1, 'prof.jose@email.com', 'Matemática'),
(2, 'prof.maria@email.com', 'História'),
(3, 'prof.ana@email.com', 'Física'),
(4, 'prof.paulo@email.com', 'Química'),
(5, 'prof.carlos@email.com', 'Geografia'),
(6, 'prof.fernanda@email.com', 'Biologia'),
(7, 'prof.luiz@email.com', 'Português'),
(8, 'prof.tiago@email.com', 'Filosofia'),
(9, 'prof.juliana@email.com', 'Sociologia'),
(10, 'prof.roberto@email.com', 'Educação Física');
