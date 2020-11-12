from flask import Flask, jsonify, request
from  data_access import db, TypingScore, my_app
from datetime import datetime


app = my_app

@app.route('/typing-score')
def get_typing_score():
    data = db.session.query(TypingScore).limit(10).all()
    result = []
    for d in data:
        result.append(d.to_dict())
    print("....Printing results....")
    print(jsonify(result))
    return {
        "value" : 0.1,
        "timestamp" : "2020-10-01T19:00:00:00",
    }

@app.route('/save-typing-score', methods=['POST'])
def insert_typing_score():
    data = request.get_json()
    print(data)
    save_typing_score(data['value'], data['timestamp'])
    return "Successfully saved"

def save_typing_score(typing_score, event_date_time):
    dt = datetime.strptime(event_date_time, '%Y-%m-%dT%H:%M:%S')
    db.session.add(TypingScore(score=typing_score, event_date=dt))
    db.session.commit()
