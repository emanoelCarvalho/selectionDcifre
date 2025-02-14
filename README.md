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
    git clone https://github.com/emanoelCarvalho/selectionDcifre
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
```

A aplicação estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa da API no navegador através do link abaixo:

- **Documentação**: [http://localhost:8000/docs](http://localhost:8000/docs)

> Você pode testar todos os endpoints diretamente pela documentação, já que o **FastAPI** fornece uma interface interativa para interagir com a API.

## Testes

Para rodar os testes do projeto, utilize o **pytest**:

```bash
pytest
```

Os testes irão verificar o correto funcionamento dos endpoints e da lógica de negócios da aplicação.

## Endpoints

- **POST /companies/**: Criar uma nova empresa.
- **GET /companies/{id}**: Buscar informações de uma empresa.
- **PATCH /companies/{id}**: Atualizar informações de uma empresa.
- **DELETE /companies/{id}**: Deletar uma empresa.
- **POST /obligations/**: Criar uma nova obrigação para uma empresa.
- **GET /obligations/{id}**: Buscar informações de uma obrigação.
- **PATCH /obligations/{id}**: Atualizar informações de uma obrigação.
- **DELETE /obligations/{id}**: Deletar uma obrigação.

---