#!/usr/bin/python3

import csv
  
with open("pokedex.txt") as pokedata:
    for x in csv.DictReader(pokedata):
        print(f'{x["Name"]} has an attack score of {x["Attack"]}.')


pokechoice= input("Choose a Pokemon:")
with open("pokedex.txt") as pokedata:
for x in csv.DictReader(pokedata):
if pokechoice in x["Name"]: print(f'{x["Name"]} has an attack score of {x["Attack"]}.')
