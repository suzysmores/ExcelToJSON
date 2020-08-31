import csv
import json

my_list = []
with open('HLR-FPSmokeAlarm.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        index = row["Assignment of Index"].replace(" " , "")
        message = row["Fault Message Banner Wording"]
        my_dict = {"Index":index, "Message": message}   
        my_list.append(my_dict)

with open('FPSmokeAlarm.json', 'w') as outfile:
    json.dump(my_list, outfile, indent= 4)

