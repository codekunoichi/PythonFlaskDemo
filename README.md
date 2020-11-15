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

## Integrating DB Connectivity

- `pip3 install sqlalchemy`
- `pip3 install flask_sqlalchemy`
- `pip3 install psycopg2-binary`
- `pip3 install simplejson` (Oddly this was a necessary install to avoid the error `TypeError: Object of type Decimal is not JSON serializable`)

## Database Setup

- `CREATE SCHEMA nqchallenge;`

- `DROP TABLE nqchallenge.TYPING_SCORE;`

  ```
    CREATE TABLE nqchallenge.TYPING_SCORE(
       TYPING_SCORE_ID SERIAL PRIMARY KEY      NOT NULL,
       SCORE           NUMERIC(10, 2)          NOT NULL,
       EVENT_DATE      TIMESTAMP               NOT NULL
    );

    CREATE SCHEMA nqchallenge;

    select * from nqchallenge.typing_score;
  ```

  ## Wiring SQLAlchemy to do basic CRUD

  ```
  class TypingScore(db.Model):
      typing_score_id = db.Column(db.Integer, primary_key=True)
      score = db.Column(db.Numeric(10,2), nullable=False)
      event_date = db.Column(db.DateTime, nullable=False)
      __table_args__ = {'schema': 'nqchallenge'}

      def __repr__(self):
          return '<TypingScore %r %r %r>' % (self.typing_score_id, self.score, self.event_date)

      def to_dict(self):
          return {
              "timestamp" : self.event_date,
              "value" : self.score
          }
  ```

- The `to_dict` method will be used for shipping API JSON output.

- Good practice - always add a `__repr__` method call for debugging purposes and printing readable object reprresentations.

- `https://docs.sqlalchemy.org/en/13/core/type_basics.html` Use this translation to map between PostgreSQL DB Data type and the equivalent type in ORM.

## Adding data to the table

```
db.session.add(TypingScore(score=0.42, event_date=datetime.now()))
db.session.add(TypingScore(score=0.25, event_date=datetime.now()))
db.session.commit()
```

The `db` handle was Initialized using the following:

```
my_app = Flask(__name__)
my_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uname:pwd@cdbhost.com'
db = SQLAlchemy(my_app)
```
