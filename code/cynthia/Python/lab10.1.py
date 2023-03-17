import requests
import json
import time
#lab10 Dad Jokes

response = requests.get('https://icanhazdadjoke.com/', headers = {'accept':'application/json'})

# print(response.text)

response_text = json.loads(response.text)
joke = response_text.get('joke')
time.sleep(2)
print(joke)
