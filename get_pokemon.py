# pip is an external package created by other people

import requests

from pprint import pprint

pokemon_number = input("What is the pokemon's ID?")
url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_number)

response = requests.get(url)
# print(response)

pokemon = response.json()
# print(pokemon["forms"])

# pprint(pokemon)
print(pokemon["name"] + "'s height is " + str(pokemon["height"]) + "cms " + "and it weighes " + str(pokemon["weight"]) + " kgs.")


# pprint => pretty print ? :D

'''
moves = pokemon["moves"]

for move in moves:
    print(move["move"]["name"])

'''

'''
Important Note : 
pprint --> use it to print dictionaries only
print --> use it to print anything 
'''




