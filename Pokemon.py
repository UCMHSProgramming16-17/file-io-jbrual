import csv
import requests

# Q: What are the fastest Flying-type Pokemon?
base_url = "http://pokeapi.co/api/v2/"
type_url = base_url + "type/"
r = requests.get(type_url + "flying/")

results = r.json()
flying_list = results["pokemon"]

csvfile = open("Flying.csv", "w")
csvwriter = csv.writer(csvfile, delimiter=',')
    
for pokemon in flying_list:
    name = pokemon["pokemon"]["name"]
    print(name)
    csvwriter.writerow([name])
    
# for pokemon in flying_list:
#     speed = pokemon["pokemon"]["url"]
#     for url in speed:
#         print(["speed"])
    
csvfile.close()