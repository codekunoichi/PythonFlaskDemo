# Demo of a basic Flask Application

## Initialize a virtual environment

we can do anything with our application within this environment, without affecting any other Python environment.

- `pip3 install virtualenv`

- `virtualenv my_flask_app`

- `cd my_flask_app`

- `source bin/activate`

- Add a basic gitignore file `echo "*.pyc" >> .gitignore`

## Install Flask Package

- `pip3 install flask`

## Simple Hello World

- Create a `hello.py` file with the following content

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## To run the hello world locally

```
export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

- On your favorite browser - Go to URL `http://localhost:5000/` to see the Hello World

## Integrating SQLAlchemy into the Flask Application

- `pip3 install sqlalchemy`

## Database Setup

- `CREATE SCHEMA nqchallenge;`

- ```
  CREATE TABLE nqchallenge.TYPING_SCORE(
   TYPING_SOCRE_ID SERIAL PRIMARY KEY      NOT NULL,
   SCORE           NUMERIC(10, 2)          NOT NULL,
   EVENT_DATE      TIMESTAMP               NOT NULL
  );
  ```
