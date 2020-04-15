from flask import Flask, request,render_template, redirect
from flask_cors import CORS,cross_origin
app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/todo/*": {"origins": "*"}})


TODOS = []

@app.route('/todo', methods=['POST', 'DELETE'])
def add_todo ():
    if request.method == 'POST':
        todo = request.form['task']
        TODOS.append(todo)
        print("Added", todo)
        return redirect('/', code=302)
    else:
        print(request.form)
        todo = request.form
        TODOS.remove(todo)
        print("deleted", todo)
        return {"Ok":'200'}

@app.route('/')
def hello_world():
    return render_template('index.html', todos=TODOS, todos_count=len(TODOS))
