from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

with open('db.json', 'r') as file:
        todos = json.load(file)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', todos=todos['todos'])


@app.route('/todo/', methods=['POST'])
def todo_list():
    data=dict(request.form)
    data['is-done']='no'
    if len(todos['todos']) == None:
         data['id'] = 1
    else:
        data['id']= todos['todos'][-1]["id"] +1
        
    todos['todos'].append(data)
    with open('db.json', 'w') as file:
          file.write(json.dumps(todos, indent=4))
    return redirect('/')

@app.route('/finished/<int:id>', methods = ['POST'])
def finished_task(id):
    data=dict(todos)
    match = list(filter(lambda todo: todo['id'] == id, data['todos']))[0]
    # x = data['todos'].index(match)
    match['is-done']='yes' 
    with open('db.json', 'w') as file:
          file.write(json.dumps(data, indent=4))
    return redirect('/')   


app.run(debug=True)