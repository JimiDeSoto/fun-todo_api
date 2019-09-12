#!flask/bin/python

from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "API http://localhost:5000/todo/api/v1.0/tasks"

tasks = [
    {
        'id': 1,
        'title': u'Zakupy',
        'description': u'Chleb, Mleko, Kefir, Masło', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Umyć samochód',
        'description': u'Myjnia przy BP, żetony w schowku', 
        'done': False
    }
]

#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#   return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
