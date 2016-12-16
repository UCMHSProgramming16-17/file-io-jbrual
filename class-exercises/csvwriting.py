import csv
import math

csvfile = open("triangles.csv", "w")
csvwriter = csv.writer(csvfile, delimiter=',')

csvwriter.writerow(["A", "B", "Hypotenuse"])

for a in range(1, 101):
    for b in range(a, 11):
        hypotenuse = math.sqrt(a ** (2) * b ** (2))
        csvwriter.writerow([a, b, hypotenuse])