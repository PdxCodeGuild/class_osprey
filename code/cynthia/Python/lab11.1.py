#Lab 11.1
#get a random quote

import requests
import json
import pprint



response = requests.get('https://favqs.com/api/qotd', headers = {'accept': 'application/json'})

quote_details = json.loads(response.text)
# pprint.pp(quote_details) #nested dictionaries
body = quote_details['quote']['body']
author = quote_details['quote']['author']

print(f'{body}  - {author}')
