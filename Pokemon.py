# Q: What are the fastest Flying-type Pokemon?
# Import the appropriate modules.
import csv, requests, operator

# Reach the API by building its URL.
base_url = "http://pokeapi.co/api/v2/type/"
type_poke = input("Select a type. ")
url = base_url + type_poke
r = requests.get(url)

# Use .json format and use the appropriate dict. key.
results = r.json()
type_list = results["pokemon"]

# Create a .csv file for export data.
csvfile = open("Speeds.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

# Establish header row.
csvwriter.writerow(["Pokemon", "Speed"])

type_pokemon = {}

# For each Pokemon, determine its name and base speed stat
# and write it to the .csv.
for pokemon in type_list:
    name = pokemon["pokemon"]["name"]
    url = pokemon["pokemon"]["url"]
    rspeed = requests.get(url)
    speed_results = rspeed.json()
    speed_list = speed_results
    speed = speed_list["stats"][0]["base_stat"]
    type_pokemon[name] = speed

sortedlist = sorted(type_pokemon, key = type_pokemon[1])

print(sortedlist)