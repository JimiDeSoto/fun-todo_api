#!flask/bin/python

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "API http://localhost:5000/todo/api/v1.0/tasks"

tasks = [
    {
        'id': 1,
        'title': u'Zakupy',
        'description': u'Chleb, Mleko, Kefir', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Umyć samochód',
        'description': u'Myjnia przy BP, żetony w schowku', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
