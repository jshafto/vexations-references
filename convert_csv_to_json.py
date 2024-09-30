import csv
import json
import os

def csv_to_json(csvFilePath, jsonFilePath):
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for ind, rows in enumerate(csvReader):
            rows["id"] = ind
            data.append(rows)
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write('const citations = ')
        jsonf.write(json.dumps(data, indent=4))
        jsonf.write('''

export default citations;''')
        

csvFilePath = f'{os.getcwd()}/Vexations - Works cited - References (Full).csv'
jsonFilePath = f'{os.getcwd()}/vexations.js'
 
csv_to_json(csvFilePath, jsonFilePath)