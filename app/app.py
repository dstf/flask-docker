import os
import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://db:27017',
                 username='root',
                 password='rootpassword')

db = client.app_db


@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'API.fixerupper.me /v1 is Up and Running'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp




@app.route('/v1')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@app.route('/v1', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='saved successfully!'
    ), 201






@app.route('/v1', methods=['DELETE'])
def deleteTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.delete_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201




@app.route('/login', methods=['POST'])
def login():
    user_records = db.user.find({'username': request.json['username']})
    return dumps(user_records)


@app.route('/v2', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


