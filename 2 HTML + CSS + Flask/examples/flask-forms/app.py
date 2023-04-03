from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/color/', methods=['GET', 'POST'])
def color_picker():
    # color = request.form.get('my-color')
    # if color is None:
    #     color = '#b1b1b1'

    color = '#b1b1b1'
    if request.method == 'POST':
        color = request.form['my-color']
    return render_template('color.html', color=color)


@app.route('/', methods=['GET'])
def index():
    return render_template('recommendations.html', books=books['books'])


@app.route('/submit-book/', methods=['POST'])
def submit():
    books['books'].append(request.form)
    with open('2 HTML + CSS + Flask/examples/flask-forms/data.json', 'w') as file:
        file.write(json.dumps(books, indent=4))
    return redirect('/')


# Whenever the app loads, it will read the data.json file
# and make its contents a globally available dictionary
with open('2 HTML + CSS + Flask/examples/flask-forms/data.json', 'r') as file:
    books = json.load(file)

app.run(debug=True)
