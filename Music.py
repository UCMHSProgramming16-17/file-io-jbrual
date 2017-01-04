import csv

musicfile = open("Rankings.csv", "w")
csvwriter = csv.writer(musicfile, delimiter = ",")

csvwriter.writerow(["Place:", "Last Week:", "Artist(s):", "Song Name:", "Peak:", "WOC:"])

count = 1

def song_input():
    place = input("Place? ")
    lw = input("Last week position? ")
    artists = input("Artist(s)? ")
    song_title = input("Song title? ")
    peak = input("Peak? ")
    WOC = input("Weeks on chart? ")
    
    songdata = [place, lw, artists, song_title, peak, WOC]
    csvwriter.writerow(songdata)

while count <= 40:
    song_input()
    count += 1

musicfile.close()