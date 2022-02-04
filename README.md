# Flask - DIP

POC Flask application to apply repository pattern, dependency injection and inversion of control.

## Installation

1. Create a virtual environment at the root of the project:

`py -m venv venv`

2. Activate virtual environment:

- CMD: `venv\Scripts\activate`
- Git Bash: `source venv/Scripts/activate`

3. Install dependencies:

`pip install -r requirements.txt`

4. Create a new Postgres database at your machine or in a container named *flask_dip*

5. Update username, password and host of the connection URL on [.env](https://github.com/Arthurdb1999/flask-dip/blob/master/.env) file at the root of the project

6. Create Tables:

`flask db_create`

7. Run the server on port 5000:

`flask run`

8. Use a REST Client to make requests to the API, such as Insomnia or Postman.

- Make a **POST** request to `http://localhost:5000/createUser`, with the following JSON body:

```
{
  "id": 1,
  "name": "Arthur"
}
```

## Tests

1. Follow previous steps until step 3 included

2. Run tests:

`pytest`

## Explanation [PT-BR]

Fiz esta POC com base principalmente em dois link:

1. [Precisamos falar de Injeção/Inversão de Dependência no Python](https://tech.pagueveloz.com.br/precisamos-falar-de-inje%C3%A7%C3%A3o-invers%C3%A3o-de-depend%C3%AAncia-no-python-f79f53fa6f54)
  - [Repositório utilizado na escrita do artigo acima](https://github.com/cassioeskelsen/precisamos-falar-de-di-ioc-python)

2. [Cosmic Python](https://www.cosmicpython.com/book/chapter_02_repository.html) (Principalmente capítulos 1, 2 e 4)
