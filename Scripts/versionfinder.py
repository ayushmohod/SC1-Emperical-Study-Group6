import json
import os
import csv

def extract_data(file_path):
    with open(file_path) as f:
        data = json.load(f)

    key_name = 'result'
    value = data[key_name]
    return value[0]['CompilerVersion']

# Define the directory where the files are located
directory = './contracts/'

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

# Open a file for writing
output_file = open('version.txt', 'w')

# Open a file for writing the counts in CSV format
csv_file = open('version.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Count'])

csv_file2 = open('version2.csv', 'w', newline='')
csv_writer2 = csv.writer(csv_file2)
csv_writer2.writerow(['Version','Count'])

# Loop through the dictionary and write the results to the output files
for result, count in counts.items():
    # output_file.write(f"{result}\n")
    csv_writer.writerow([count])
    csv_writer2.writerow([result,count])
    # csv_writer2.write(['Version','count'])
    output_file.write(f"{result}: {count}\n")

# Loop through the dictionary and write the results to the output file
# for result, count in counts.items():
#     output_file.write(f"{result}: {count}\n")

# Close the output file
output_file.close()
csv_file.close()
# csv_file2.close()
