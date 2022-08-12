#!/usr/bin/python3

import requests

URL = "https://pokeapi.co/api/v2/pokemon"

def main():
    pokemon = requests.get(f"{URL}?limit=151")
    pokemon = pokemon.json()

    for poke in pokemon["results"]:
        print(poke.get("name"))

    print(f"Total number of Pokemon in Generation 1: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()
