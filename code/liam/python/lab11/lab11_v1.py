import requests
#
# v1: Display one (1) random quote and it's author


response = requests.get('https://favqs.com/api/qotd', 
    headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},)

quote_pull = response.json()
#quote_pull is dict
'''{
    'qotd_date': '2023-03-16T00:00:00.000+00:00', 
    'quote': {'id': 48639, 'dialogue': False, 'private':ites_count': 2, 
    'upvotes_count': 1, 'downvotes_count': 0, 'author': 'Aristotle', 
    'author_permalink': 'aristotle', 
    'body': 'What it lies in our power to do, it lies in our power not to do.'}}
    
    first two keys are 'qotd_date' (useless) and 'quote' (everything we want is in here)'''

quote = quote_pull['quote']['body']
author = quote_pull['quote']['author']

print(f'''The random quote is...

    {author} - {quote}

wow.
''')