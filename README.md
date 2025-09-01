# Projeto Workout API


Uma API RESTful para gerenciar atletas, categorias e centros de treinamento, construída com FastAPI e SQLModel. O projeto simula o cadastro e gestão de dados de uma academia, permitindo operações de criação, leitura, atualização e exclusão de informações.




## Como rodar

1. Clone este repositório.
2. Instale as dependências com Poetry:


```poetry install```

3. Inicie o servidor Uvicorn:

```task run```



## Estrutura do projeto

.
├── workout_project/
│   ├── __pycache__/
│   ├── db/
│   │   ├── __pycache__/
│   │   ├── dependencies.py
│   │   ├── engine.py
│   │   └── models.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── atleta.py
│   │   ├── categoria.py
│   │   └── centro_treinamento.py
│   ├── repositories/
│   │   ├── __pycache__/
│   │   ├── atleta.py
│   │   ├── categoria.py
│   │   └── centro_treinamento.py
│   ├── routes/
│   │   ├── __pycache__/
│   │   ├── atleta.py
│   │   ├── categoria.py
│   │   └── centro_treinamento.py
│   └── schemas/
│       ├── __pycache__/
│       ├── atleta.py
│       ├── categoria.py
│       └── centro_treinamento.py
├── .env.example
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── ...


## Funcionalidades

- [x] Cadastra Atleta
- [x] Cadastra Centro de Treinamento
- [x] Cadastra Categoria
- [x] Lista atletas, centro de treinamento e categoria
- [x] Busca atletas, centro de treinamento e categorias

## Redes Sociais

[![linkedin](https://img.shields.io/badge/linkedin-000?style=for-the-badge&logo=linkedin&logoColor=blue)](https://www.linkedin.com/in/daniel-almeida-822332165/)

[![instagram](https://img.shields.io/badge/instagram-000?style=for-the-badge&logo=instagram&logoColor=blue)](https://www.instagram.com/dhantaro/)