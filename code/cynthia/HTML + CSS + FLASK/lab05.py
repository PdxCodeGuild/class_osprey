# lab05 Flask Form Using Python Lab01.2

from flask import Flask, render_template, request, redirect
import json
from number_conversion import convert_number

app = Flask(__name__)


# with open('data.json', 'r') as file:
#     number = json.load(file)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



    number = convert_number()
# @app.route('/number/', methods=['POST'])
# def number_list():
#     convert_number('enter-number')
#     number= dict(request.form)
#     number['number'].append(number)
#     # with open('data.json', 'w') as file:
#     #     file.write(json.dumps(number))
#     return redirect('/')



# @app.route('/submit-number', methods=["POST"])
# def submit():
#     number['enter-number'].append(request.form)
#     with open('data.json', 'w') as file:
#         file.write(json.dumps(number))
#     return redirect('/')


app.run(debug=True)