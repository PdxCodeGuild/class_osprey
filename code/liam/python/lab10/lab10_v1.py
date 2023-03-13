#Dad Jokes API
from time import sleep
import requests

response = requests.get('https://icanhazdadjoke.com/', 
    headers={'Accept': 'application/json'},)

dad_joke = response.json()

if '? ' in dad_joke['joke']:
    halves = dad_joke['joke'].split('? ')
    print(f'{halves[0]}?')
    sleep(3)
    print(halves[1])
elif '. ' in dad_joke['joke']:
    halves = dad_joke['joke'].split('? ')
    print(f'{halves[0]}.')
    sleep(3)
    print(halves[1])
else:
    print(dad_joke['joke'])