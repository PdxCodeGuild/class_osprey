'''
URL - Uniform Resource Locator

https://mail.google.com/mail/u/0/#inbox

[protocol]://[*subdomain].[domain].[extension/TLD]/*path/*to/*wherever?query_params=extra_info&next_param=thing_two#place-on-the-page

when you hit a URL in your browser
- your ISP sends it to your DNS (Domain Name Server) (the address book of the internet)
- the DNS resolves it into an IP address
- a request (in this case, an HTTP request) is sent to that address
- whoever is on the other end interprets your request and sends a response
- the response comes back in more or less the same way it went
- then the response can be interpreted by you
    (your browser reading the html/css/JS, or you parsing the JSON, etc)

    
HTTP methods:
- GET (this is the one your browser uses when you hit a URL)
- POST
- PUT
- PATCH
- DELETE
- plus some weird ones like HEAD and OPTIONS

'''


import requests
import pprint
import json


query_params = {
    'results': 3,
    'nat': 'IR',
    'gender': 'female'
}

# you can pass the parameters as part of the URL
response = requests.get(
    'https://randomuser.me/api/?results=3&nat=IR&gender=female')

# or you can pass them as a dict with the 'params' keyword argument
response = requests.get('https://randomuser.me/api/', params={'results': 3})

# for this API we don't need to specify headers, but some APIs require headers
response = requests.get('https://randomuser.me/api/',
                        params=query_params, headers={'accept': 'application/json'})


# response.text is a string
print(response.text)

# parses the response text into a dictionary
response_text = response.json()
# pretty much the same thing
response_text = json.loads(response.text)

# pprint.pprint(response_text)

# access the nested data structure, one layer at a time
name = response_text['results'][1]['name']

print(f"{name['title']}. {name['first']} {name['last']}")
