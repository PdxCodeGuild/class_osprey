import requests
import json
import time
#lab10 Dad Jokes
#version 2: allow the user to search for jokes

query_params = {}
query_params["search_term"] = input('')
print(query_params)


response = requests.get(f'https://icanhazdadjoke.com/', params=query_params, headers = {'accept':'application/json'})

# print(response.text)

response_text = json.loads(response.text)
joke = response_text.get('joke')
#time.sleep(2)
print(joke)
