from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

tasks = [
    {
        'id': 1,
        'Name': 'Praveen',
        'Employee ID': 'gur46682',
        'Billable': True
    },
    {
        'id': 2,
        'Name': 'Kumar',
        'Employee ID': 'gur49983',
        'Billable': True
    }
]

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( {'tasks':tasks} )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'Name' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Employee ID': request.json.get('Employee ID', ""),
        'Billable': False
    }
    tasks.append(task)
    return jsonify( {'task':task} ), 201
if __name__ == '__main__':
    app.run(debug = True)
