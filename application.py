from flask import Flask, render_template, request, jsonify, url_for, redirect
from pymongo import MongoClient
import os
from dotenv import load_dotenv

client = MongoClient('mongodb+srv://sparta3:test@cluster0.jfmyzub.mongodb.net/?retryWrites=true&w=majority')

load_dotenv()

db_url = os.getenv('mongodb+srv://sparta3:test@cluster0.jfmyzub.mongodb.net/?retryWrites=true&w=majority')

client = MongoClient(db_url)
db = client.dbsparta
application = Flask(__name__)#위치 바꿈 안되면 위로

@application.route('/')
def home():
    return render_template('login.html')


@application.route("/userInfo", methods=["POST"])
def send_user_PasswordANDloginID():
    email_Info= request.form['user_email']
    password_Info = request.form['login-password']


    doc = {
        'email_Info': email_Info,
        'password_Info': password_Info 
    }

    db.user.insert_one(doc)
    return render_template("login.html")

    
    









if __name__ == '__main__':
    application.run('0.0.0.0', port=5001, debug=True)
    # application.run()