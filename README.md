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

## Wiring API Logic

- URL mapping will be via `@app.route('/typing-score')`
- As you can see this mini web application will have access to URLs `'/typing-score'`, `'/save-typing-score'`
- For each URL define what the method will do behind the scene.
- The most convenient package to transform and adhere to JSON output would be `jsonify` import that

```
@app.route('/typing-score')
def get_typing_score():
    data = db.session.query(TypingScore).limit(10).all()
    result = []
    for d in data:
        result.append(d.to_dict())
    return jsonify(result)

@app.route('/save-typing-score', methods=['POST'])
def insert_typing_score():
    data = request.get_json()
    save_typing_score(data['value'], data['timestamp'])
    return "Successfully saved"

def save_typing_score(typing_score, event_date_time):
    dt = datetime.strptime(event_date_time, '%Y-%m-%dT%H:%M:%S')
    db.session.add(TypingScore(score=typing_score, event_date=dt))
    db.session.commit()
```

## How to access API end point once you run the Flask Application

- `export FLASK_APP=test_score_app.py`
- `flask run`

- To post typing score use the following command to test

```
curl -X POST http://localhost:5000/save-typing-score -H 'content-type: application/json' -d '{"value":
0.1, "timestamp": "2020-10-01T19:00:00"}' -i
```

Please note the URL change - `save-typing-score`

- To retreive typing score use the following command `curl http://localhost:5000/typing-score`

## Pinciples followed for clean coding

- Keep it short - Having no more than 10 lines of code per method for ease of readability
- Single Responsibility Principle - Each function doing only one thing and no more. Hence do not be afraid to make small utility methods like `save_typing_score`

## Room for improvement

- config file to not hard code the DB URL.
- Bette separation - introduce abstraction to separate UI knowing from having the presence of DB - and DB knowing UI will use it.
- Flask Route Testiing.
- Due to limited time for submission, I have kept the code functional but I would probably revisit and separate the `save_typing_score` method to encapsulate interaction with DB. Such that a standalone application can equally use the save method besides the UI application.
