import requests
import json

# postcodes api

# postcodes_req = requests.get('https://api.postcodes.io/postcodes/se120nb')
#
# print(postcodes_req)  # <Response [200]>
# print(postcodes_req.status_code)  # 200
# # print(postcodes_req.content)  # returns content from the uri as bytes
# # print(postcodes_req.json())  # turns content into a python dict
#
# json_body = json.dumps({'postcodes': ['PR3 0SG', 'M45 6GN', 'EX165BL']})
# headers = {'content-type': 'application/json'}
#
# post_multi_req = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)
#
# print(post_multi_req.json())

# pokemon api

pokemon_req = requests.get('https://pokeapi.co/api/v2/pokemon/celebi')

# print(pokemon_req.json())

# BBC requests

bbc_request = requests.get('https://www.bbc.co.uk/')

# print(bbc_request.content)
