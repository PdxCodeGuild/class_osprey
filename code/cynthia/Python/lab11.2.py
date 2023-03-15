#Lab 11.2
#list quotes by keyword

import requests
import json
import pprint

user_keyword = input('enter a keyword to search for quotes: ')
query_params = {}
query_params["filter"] = user_keyword
print(query_params)

response = requests.get('https://favqs.com/api/quotes/',params = query_params , headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quote_details = json.loads(response.text)
pprint.pp(quote_details) 

# body = quote_details['quote']['body']
# author = quote_details['quote']['author']

# print(f'{body}  - {author}')

#repl
