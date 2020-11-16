from flask import Flask, jsonify, request
from  data_access import db, TypingScore, my_app, save, find_last_10
from datetime import datetime


app = my_app

@app.route('/typing-score')
def get_typing_score():
    result = find_last_10()
    #print("....Printing results....")
    return jsonify(result)

@app.route('/typing-score', methods=['POST'])
def insert_typing_score():
    data = request.get_json()
    #print(data)
    save(data['value'], data['timestamp'])
    return "Successfully saved"
