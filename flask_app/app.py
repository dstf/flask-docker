from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)


@server.route('/', )
def hello_world():
        return 'The model is up and running. Send a POST request'
   

@server.route('/api')
def hello_api():
        return 'Send an API request'
   
