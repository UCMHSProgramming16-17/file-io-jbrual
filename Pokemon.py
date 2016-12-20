import csv
import requests
import operator

# Q: What are the fastest Flying-type Pokemon?
base_url = "http://pokeapi.co/api/v2/"
type_url = base_url + "type/"
r = requests.get(type_url + "flying/")

results = r.json()
flying_list = results["pokemon"]

csvfile = open("Flying.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

csvwriter.writerow(["Pokemon", "Speed"])
    
for pokemon in flying_list:
    name = pokemon["pokemon"]["name"]
    url = pokemon["pokemon"]["url"]
    rspeed = requests.get(url)
    speed_results = rspeed.json()
    speed_list = speed_results
    speed = speed_list["stats"][0]["base_stat"]
    csvwriter.writerow([name, speed])

csvsort = open("Flying.csv", "r")
csvreader = csv.reader(csvsort, delimiter = ",")
sort = sorted(csvreader,key=operator.itemgetter(1))

for line in sort:
    csvwriter.writerow([name, speed])

csvfile.close()