from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient


application = Flask(__name__)

client = MongoClient('')
db = client.dbsparta


@application.route('/')
def home():
    return 'hello, world!'


if __name__ == '__main__':
    # application.run('0.0.0.0', port=5001, debug=True)
    application.run()