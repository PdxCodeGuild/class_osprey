from flask import Flask, render_template, request

app = Flask(__name__)


PEOPLE = [
    {"name": "Liam", "role": "student", 'class': 'Osprey'},
    {"name": "Cynthia", "role": "student", 'class': 'Osprey'},
    {"name": "Danny", "role": "instructor", 'class': 'Osprey, Orchid, Opal'},
    {"name": "James", "role": "TA", 'class': 'Osprey'},
]


def triple_number(n):
    return n*3


@app.route('/')
def hello_world():
    context = {
        "class_name": "Class Osprey",
        "start_date": 'February 27, 2023',
        "grad_date": "June 9, 2023",
        "people": PEOPLE,
        "repo": 'https://github.com/PdxCodeGuild/class_osprey',
        "lucky_numbers": [7, 13, 2],
        "triple": triple_number
    }
    return render_template('index.html', context=context)


@app.route('/<string:name>')
def person(name):
    person = list(filter(lambda p: p["name"].lower() == name.lower(), PEOPLE))
    if len(person) > 0:
        bonus_content = ''
        try:
            bonus_content = f"and their favorite food is {request.args['food']}"
        except:
            pass
        return f"{person[0]['name']} is a {person[0]['role']} in Class {person[0]['class']} {bonus_content}"
    return "That person is not at PDX Code Guild"


app.run(debug=True)
