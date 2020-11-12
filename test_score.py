from flask import Flask
app = Flask(__name__)

@app.route('/typing-score')
def get_typing_score():
    return {
        "value" : 0.1,
        "timestamp" : "2020-10-01T19:00:00:00",
    }

@app.route('/save-typing-score')
def save_typing_score():
    my_val = {
        "value" : 0.1,
        "timestamp" : "2020-10-01T19:00:00:00"
    }
    return "Successfully saved!"
