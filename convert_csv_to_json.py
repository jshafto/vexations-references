import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path, list_name):
    data = []
     
    # Open a csv reader called DictReader
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for ind, rows in enumerate(csvReader):
            rows["id"] = ind
            data.append(rows)
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(f'const {list_name} = ')
        jsonf.write(json.dumps(data, indent=4))
        jsonf.write(f'''

export default {list_name};''')
        
list_name = 'citations'
csv_file_path = f'{os.getcwd()}/Vexations - Works cited - References (Full).csv'
json_file_path = f'{os.getcwd()}/public/citations.js'


list_name2 = 'additional'
csv_file_path2 = f'{os.getcwd()}/additional-references.csv'
json_file_path2 = f'{os.getcwd()}/public/additional.js'
 
csv_to_json(csv_file_path, json_file_path, list_name)
csv_to_json(csv_file_path2, json_file_path2, list_name2)