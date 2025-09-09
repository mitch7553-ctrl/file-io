import pandas as pd
#import numpy as np
import csv 
filename = "spotify-2023.csv"
fields = []
rows = []

data = pd.read_csv(filename, encoding="ISO-8859-1")  
  
#Read data from the CSV file
def getDData(reader):
  with open(filename, 'r') as f: 
    reader =csv.reader(f) 
    fields = next(reader)
    for row in reader:
      rows.append(row)
      print(row)


#Solution one, get the nummber of songs in the dataset
def countSongs(data):
  return data.loc[:,"track_name"].count()


getDData(rows)
print("Number of songs in the dataset: ", countSongs(data))
print(data["key"])