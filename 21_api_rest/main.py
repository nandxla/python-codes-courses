import requests 
import json 

rick_morty_characters = requests.get('https://rickandmortyapi.com/api/character')
characters = rick_morty_characters.json()['results'] 

for character in characters:
    print(character['name'])
    print(character['image'])
    print()
