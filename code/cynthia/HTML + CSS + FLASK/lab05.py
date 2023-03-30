# lab05 Flask Form Using Python Lab01.2
# may not need the json file

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])
def number_conversion():
    return render_template('lab05.html')