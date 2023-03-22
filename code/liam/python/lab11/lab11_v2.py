import requests
#
# v2: list quotes by keyword
# implement pagination and custom keyword entry

def search(page, keyword):
    query_params = {
        'page' : page,
        'filter': keyword,
    }
    response = requests.get('https://favqs.com/api/quotes?page='+page+'&filter='+keyword, 
        headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
        params=query_params)

    quote_pull = response.json()

    for i in range(len(quote_pull['quotes'])):
        quote = quote_pull['quotes'][i]['body']
        author = quote_pull['quotes'][i]['author']
        print(f'{author} - {quote} \n')

    page_track = quote_pull['last_page']

    if page_track == False:
        return page_track
    return True

#REPL
while True:
    keyword = input('What would you like to see quotes about? ')
    page = '1'

    while search(page, keyword) == False:
        print(f'End of page {page}.')
        next = input('enter \'next page\' or \'done\': ')
        if next == 'next page':
            page_append = int(page) + 1
            page = str(page_append)
        elif next == 'done':
            keyword = input('What would you like to see new quotes about? ')
            page = '1'

    again = input(f'End of quotes about {keyword}. Search again? ').lower()
    yes = ['y', 'yes', 'ok']
    if again in yes:
        continue
    break