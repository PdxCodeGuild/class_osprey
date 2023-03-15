import requests
import json
import time
#lab10 Dad Jokes
#version 2: allow the user to search for jokes

query_params = {}
query_params["term"] = input('')
print(query_params)


response = requests.get(f'https://icanhazdadjoke.com/search', params=query_params, headers = {'accept':'application/json'})

# print(response.text)

response_text = json.loads(response.text)
# print(response_text)
joke = response_text.get('results')[0]['joke']
time.sleep(2)
print(joke)
