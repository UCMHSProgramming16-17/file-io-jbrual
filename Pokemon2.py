# Q: What are the fastest Flying-type Pokemon?
# Import the appropriate modules.
import csv, requests, operator

base_url = "http://pokeapi.co/api/v2/type/"
type_poke = input("Select a type. ")
url = base_url + type_poke

r = requests.get(url)
results = r.json()