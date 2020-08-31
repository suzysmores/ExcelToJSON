import csv
import json

my_list = []
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        index = row["name"].replace(" " , "")
        message = row["age"]
        my_dict = {"Name":name, "Age": age}   
        my_list.append(my_dict)

with open('testing.json', 'w') as outfile:
    json.dump(my_list, outfile, indent= 4)

