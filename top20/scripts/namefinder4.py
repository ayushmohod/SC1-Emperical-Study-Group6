import csv
import json
import os

def extract_data(file_path):
    with open(file_path) as f:
        data = json.load(f)

    key_name = 'result'
    value = data[key_name]
    return value[0]['ContractName']

# Define the directory where the files are located
directory = './top20json/'

# Create a dictionary to keep track of counts
counts = {}

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        result = extract_data(file_path)
        if result in counts:
            counts[result] += 1
        else:
            counts[result] = 1

# Open a file for writing the ContractName values
output_file = open('counts_name.txt', 'w')

# Open a file for writing the counts in CSV format
csv_file = open('counts_name.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ContractName', 'Count'])

# Loop through the dictionary and write the results to the output files
for result, count in counts.items():
    output_file.write(f"{result}\n")
    csv_writer.writerow([result, count])

# Close the output files
output_file.close()
csv_file.close()
