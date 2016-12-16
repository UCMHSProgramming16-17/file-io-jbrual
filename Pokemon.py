import csv
import requests

# Q: What are the fastest Flying-type Pokemon?

csvfile = open("PokeData.csv", "w")
csvwriter = csv.writer(csvfile, delimiter=',')