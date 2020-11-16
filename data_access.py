from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

my_app = Flask(__name__)
my_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:XXX@cc03942.localhost.com'
db = SQLAlchemy(my_app)


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

def find_last_10():
    data = db.session.query(TypingScore).limit(10).all()
    result = []
    for d in data:
        result.append(d.to_dict())
    return result

def count_records():
    return db.session.query(TypingScore).count()

def save(typing_score, event_date):
    dt = datetime.strptime(event_date, '%Y-%m-%dT%H:%M:%S.%f')
    db.session.add(TypingScore(score=typing_score, event_date=dt))
    db.session.commit()

#print(count_records())
#save(0.99, '2020-11-16T03:40:43.968688')
#print(count_records())
#db.session.add(TypingScore(score=0.49, event_date=datetime.now()))
#db.session.add(TypingScore(score=0.25, event_date=datetime.now()))
#db.session.commit()
