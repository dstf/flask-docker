import os
import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from flask_pymongo import PyMongo


app = Flask(__name__)
api = Api(app)



@app.route("/")
def get_initial_response():
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'API is Up and Running'
    }
    resp = jsonify(message)
    return resp



@app.route('/v1')
def hello_world():
       return '0'



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


