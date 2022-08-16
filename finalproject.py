#!/usr/bin/python3

import requests
import time
import csv

URL = "https://pokeapi.co/api/v2/pokemon"

def pokelist():
    pokemon = requests.get(f"{URL}?limit=151")
    pokemon = pokemon.json()

    for poke in pokemon["results"]:
        print(poke.get("name"))

def main():
    print("Welcome to the Pokedex")
    time.sleep(1)
    print("Search for Pokemon: Press 1\nFull list of Pokemon: Press 2\nType matchups: Press 3")
    choice=input(">")
    # asks for pokemon name then returns name, id, type, attack, and defense vertically
    if choice == "1":
        pokechoice.lower() = input("Choose a Pokemon:")
        with open("pokedex.txt") as pokedata:
        for x in csv.DictReader(pokedata):
        if pokechoice in x["Name"]: print(f'{x["Name"]}\n{x["#"]}\n{x["Type 1"]}\n{x["Attack"]}\n{x["Defense"]}')
    
    # prints the 151 pokemon in gen 1
    elif choice == "2":
        for poke in pokemon["results"]:
        print(poke.get("name"))
    print(f"Total number of Pokemon in Generation 1: {len(pokemon['results'])}")
    
    # is it bad to hardcode type matchups? 
    elif choice == "3":
        kind=input("What type of Pokemon would you like to know about?")

    # bring user back to initial prompt if request is not found
    # can I have it say "Please try again" or no because choice=input was defined above?
    else:
        choice = input(">")

    if __name__ == "__main__":
        main()

    # maybe add pictures or evolution information 
