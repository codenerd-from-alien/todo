from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# 1. Users
# id int
# userName varchar
# password varchar

# 2. todo
# id int
# user_id int
# context varchar
# status varchar('0', '1')

application = Flask(__name__)

client = MongoClient('mongodb+srv://home:test@cluster0.qetetie.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@application.route('/')
def home():
    return render_template('index.html')

#POST
@application.route("/todo-list", methods=["POST"])
def todo_post():
    # user_id_receive = request.form['user_id_give']
    # status_receive = request.form['status_give']
    context_receive = request.form['context_give']
    todo_list = list(db.todo.find({}, {'_id': False}))
    count = len(todo_list) + 1 

    doc = {
        'id' : count,
        'user_id' : 2,
        # 'status' : status_receive,
        'context' : context_receive
    }

    db.todo.insert_one(doc)
    
    return jsonify({'msg': '저장완료!'})


# 유저별 GET
@application.route("/todo-list", methods=["GET"])
def todo_get():
    # 아 그럼 find메서드를 활용해서 
    # 해당 user_id값과 일치하는 아이템들을
    # db에서 불러와 리스트짜고 반복문 돌리면 되겠네요?

    # 해당 user_id값과 일치하는 아이템

    # user_id = 1
    # 변수 = DB_todo 리스트 조회
    todo_list = list(db.todo.find({'user_id':1},{'_id':False}))
    return jsonify({'result': todo_list})

# Delete_id컬럼으로 삭제 값 판단
@application.route("/todo-list/delete", methods=["POST"])
def todo_delete():
    id_receive = request.form['id_give']
    db.todo.delete_one({'id':int(id_receive)})
    return jsonify({'msg': '삭제 완료!'})
# db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})

if __name__ == '__main__':
    application.run('0.0.0.0', port=5001, debug=True)
    # application.run()
