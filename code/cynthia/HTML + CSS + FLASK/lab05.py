# lab05 Flask Form Using Python Lab01.2

from flask import Flask, render_template, request, redirect

from number_conversion import convert_number

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    phrase= ''
    if request.method == 'POST':
        number = request.form['enter-number']
        phrase = convert_number(int(number))
        print(phrase)
    return render_template('index.html', phrase= phrase)


app.run(debug=True)