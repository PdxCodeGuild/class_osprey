#Dad Jokes API
#with search function
import requests

while True:
    subject = input('What would you like a dad joke about? ')

    query_params = {
        'page': 1,
        'limit': 20,
        'term': subject
    }

    response = requests.get('https://icanhazdadjoke.com/search', 
        headers={'Accept': 'application/json'}, params=query_params)

    dad_joke = response.json()

    while True:
        for joke in range(len(dad_joke['results'])):
            if joke == IndexError:
                break
            print(dad_joke['results'][joke]['joke'])
            next = input('Hit enter to continue.')
            if next != '':
                break
        break

# dict_keys(['current_page', 'limit', 'next_page', 'previous_page', 'results', 'search_term', 'status', 'total_jokes', 
# 'total_pages'])

    loop = input('Would you like to enter a new search? (y/n): ')
    if loop == 'y':
        continue
    else:
        print('Bye!')
        break