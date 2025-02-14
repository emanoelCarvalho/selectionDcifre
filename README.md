# Projeto de Gestão de Empresas e Obrigações

Este projeto é uma API desenvolvida com **FastAPI** para gerenciar empresas e suas obrigações acessórias. A API permite realizar operações CRUD (Create, Read, Update, Delete) para empresas e obrigações associadas.

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construção da API.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **PostgreSQL**: Banco de dados relacional.
- **Pydantic**: Para validação de dados.
- **pytest**: Para testes unitários.
- **Uvicorn**: Servidor ASGI para execução da aplicação.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até a pasta do projeto:

    ```bash
    cd seu-repositorio
    ```

3. Crie e ative um ambiente virtual:

    - No **Windows**:
    
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    - No **Linux/Mac**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

## Executando a Aplicação

Para rodar a aplicação em modo de desenvolvimento, utilize o **Uvicorn**:

```bash
uvicorn main:app --reload
