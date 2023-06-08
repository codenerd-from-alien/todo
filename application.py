from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

application = Flask(__name__)

load_dotenv()

db_url = os.getenv('MONGO_DB_URL')

client = MongoClient(db_url)
db = client.dbsparta


@application.route('/')
def home():
    return 'hello, world!'


if __name__ == '__main__':
    application.run('0.0.0.0', port=5001, debug=True)
    # application.run()