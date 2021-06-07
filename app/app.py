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
                  username='davide',
                  password='davide,123')
db = client.app_db


@app.route("/")
def get_initial_response():
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'API is Up and Running on /v1 folder'
    }
    resp = jsonify(message)
    return resp


@app.route('/v1')
def dev():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
                'id': str(todo['_id']),
                'username': todo['username'],
                'message': todo['message']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )

@app.route('/v1', methods=['POST'])
def create_dev():
    data = request.get_json(force=True)
    item = {
            'username': data['username'],
            'message': data['message']
           # 'message': data['message']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='saved successfully!'
    ), 201



@app.route('/v1', methods=['DELETE'])
def delete_dev():
    data = request.get_json(force=True)
    item = {
            'username': data['username'],
            'message': data['message']

    }
    db.todo.delete_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201




if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)




