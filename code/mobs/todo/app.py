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

    todos['todos'].append(request.form)
    with open('db.json', 'w') as file:
          file.write(json.dumps(todos, indent=4))
    return redirect('/')

app.run(debug=True)