# lab05 Flask Form Using Python Lab01.2

from flask import Flask, render_template, request, redirect
import json
from number_conversion import convert_number

app = Flask(__name__)

convert_number()



@app.route('/', methods=['GET'])
def number_conversion():
    number = x
    return render_template('lab05.html', number=number['enter_number'] )


@app.route('/submit-number', methods=["POST"])
def submit():
    number['enter-number'].append(request.form)
    with open('code/cynthia/HTML + CSS + FLASK/lab05.json', 'w') as file:
        file.write(json.dumps(number))
    return redirect('/')

with open('code/cynthia/HTML + CSS + FLASK/lab05.json', 'r') as file:
    number = json.load(file)



app.run(debug=True)