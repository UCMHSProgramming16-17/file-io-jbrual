# Q: What are the fastest Flying-type Pokemon?
# Import the appropriate modules.
import csv, requests, operator

# Reach the API by building its URL.
base_url = "http://pokeapi.co/api/v2/"
type_url = base_url + "type/"
r = requests.get(type_url + "flying/")

# Use .json format and use the appropriate dict. key.
results = r.json()
flying_list = results["pokemon"]

# Create a .csv file for export data.
csvfile = open("Flying.csv", "w")
csvwriter = csv.writer(csvfile, delimiter = ",")

# Establish header row.
csvwriter.writerow(["Pokemon", "Speed"])

# For each Pokemon, determine its name and base speed stat
# and write it to the .csv.
for pokemon in flying_list:
    name = pokemon["pokemon"]["name"]
    url = pokemon["pokemon"]["url"]
    rspeed = requests.get(url)
    speed_results = rspeed.json()
    speed_list = speed_results
    speed = speed_list["stats"][0]["base_stat"]
    csvwriter.writerow([name, speed])

data = csv.reader(open("Flying.csv"), delimiter = ",")
sortedlist = sorted(data, key = operator.itemgetter(1))
csvwriter.writerow(sortedlist)

# Close the .csv.
csvfile.close()