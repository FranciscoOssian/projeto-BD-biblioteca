# projeto-BD-biblioteca

https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer

# Biblioteca Python com SQLite3

Este projeto é uma biblioteca simples para gerenciar dados de uma biblioteca (alunos, livros, etc.) usando Python e SQLite3.

## Estrutura

```
biblioteca/
├── database/        # Lógica do banco de dados
│   ├── queries/       # Arquivos SQL
│   │   ├── create/
│   │   ├── read/
│   │   ├── update/
│   │   └── delete/
│   ├── services/      # Lógica de negócios
│   ├── models/        # Representação dos dados
│   └── utils.py       # Auxiliares
├── main.py          # Executa a aplicação
├── README.md        # Este arquivo
```

services são objetivos para lógica de negócios (fazer algo, fazer tal ação, como o crud por exemplo pelo banco de dados).
Existirá um service para cada tabela

models são objetos usados para trefegar os dados pelo sistema, ele carrega os campos nomeados que cada item de tabela tem.
