#!/usr/bin/python3

import requests
import time
import csv

URL = "https://pokeapi.co/api/v2/pokemon"

def main():
    while True:
        print("Welcome to the Pokedex")
        time.sleep(2)
        print("Search for Pokemon: Press 1\nSearch by type: Press 2\nFull list of Pokemon: Press 3\nType matchups: Press 4")
        choice=input(">")
        if choice == "1":
            pokechoice = input("Please choose a Pokemon:\n").lower()
            with open("pokedex.txt") as pokedata:
                for x in csv.DictReader(pokedata):
                    if pokechoice in x["Name"].lower(): 
                        print(f'Name...{x["Name"]}\nID Number...{x["#"]}\nType...{x["Type 1"]}\nAttack...{x["Attack"]}\nDefense...{x["Defense"]}')
       
        elif choice == "2":
           poketype = input("Please enter a type:\n").lower()
           with open("gen1types.txt") as types:
                    for x in csv.DictReader(types):
                        if poketype in x["Type"].lower():
                            print(f'{x["Type"]} Pokemon in Generation 1 Include:\n{x["Pokemon"]}')

        elif choice == "3":
            pokemon = requests.get(f"{URL}?limit=151")
            pokemon = pokemon.json()

            for poke in pokemon["results"]:
                print(poke.get("name"))

            print(f"Total number of Pokemon in Generation 1 is {len(pokemon['results'])}")

        elif choice == "4":
            pokematchup = input("Please enter a type:\n").lower()
            with open("typematchups.txt") as matchups:
                    for x in csv.DictReader(matchups):
                        if pokematchup in x["Type"].lower():
                            print(f'Strong against...{x["Strong"]}\nWeak against...{x["Weak"]}\nImmune to...{x["Immune"]}')

        elif choice == "exit":
            break
if __name__ == "__main__":
    main()


# when invalid entry occurs, go back to same prompt and not all the way back to "welcome
# to pokedex"

# add spaces or something to separate input from output
