#!/usr/bin/python3
  
import requests
import time
import csv

URL = "https://pokeapi.co/api/v2/pokemon"

#def pokelist():
    #pokemon = requests.get(f"{URL}?limit=151")
    #pokemon = pokemon.json()

    #for poke in pokemon["results"]:
        #print(poke.get("name"))

def main():
    while True:
        print("Welcome to the Pokedex")
        time.sleep(1)
        print("Search for Pokemon: Press 1\nFull list of Pokemon: Press 2\nType matchups: Press 3")
        choice=input(">")
        if choice == "1":
            pokechoice = input("Choose a Pokemon:\n").lower()
            with open("pokedex.txt") as pokedata:
                for x in csv.DictReader(pokedata):
                    if pokechoice in x["Name"].lower():
                        print(f'Name...{x["Name"]}\nID Number...{x["#"]}\nType...{x["Type 1"]}\nAttack...{x["Attack"]}\nDefense...{x["Defense"]}')

        elif choice == "2":
            pokemon = requests.get(f"{URL}?limit=151")
            pokemon = pokemon.json()

            for poke in pokemon["results"]:
                print(poke.get("name"))

            print(f"Total number of Pokemon in Generation 1: {len(pokemon['results'])}")
       
      # elif choice == "3":
            #kind=input("What type of Pokemon would you like to know about?")
        elif choice == "exit":
            break
# add dictionary 
if __name__ == "__main__":
    main()
