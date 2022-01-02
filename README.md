# Flask - DIP

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
