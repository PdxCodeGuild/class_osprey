from flask import Flask, render_template, request

app = Flask(__name__)

ones_table = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: '',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
}

tens_table = {
    0: 'oh',
    1: 'null',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

tenteens_table = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}


@app.route('/')
def num_to_phrase():
    return render_template('index.html')

@app.route('/phrase/', methods=['POST'])
def phrase_post():

    time = request.form['numtime']
    if len(time) == 4:
        hour = time[0]
        minutes = time[2] + time[3]
    elif len(time) == 5:
        hour = time[0] + time[1]
        minutes = time[3] + time[4]

    hour = int(hour)
    minutes = int(minutes)
    m_tens_digit = minutes//10
    m_ones_digit = minutes%10

    if hour < 10:
        english_hour = ones_table[hour]
    elif hour >= 10 and hour <= 12:
        english_hour = tenteens_table[hour]

    english_tens = tens_table[m_tens_digit]
    english_ones = ones_table[m_ones_digit]

    if minutes == 00:
        phrasetime = f'The time is {english_hour} o\'clock.'
    elif minutes >= 10 and minutes <= 19:
        tenteens = tenteens_table[minutes]
        phrasetime = f'The time is {english_hour} {tenteens}.'
    else:
        phrasetime = f'The time is {english_hour} {english_tens} {english_ones}.'

    return render_template('phrase.html', time=time, phrasetime=phrasetime)

app.run(debug=True)