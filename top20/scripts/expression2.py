import csv

# with open('version2.csv', 'r') as csv_file:
with open('version2.csv', 'r') as input_file, open('version3.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=['Version', 'Count'])
    writer.writeheader()
    for row in reader:
        version = row['Version']
        version = version.split('+')[0].split('-')[0] # keep everything before the first '+' or '_'
        count = row['Count']
        writer.writerow({'Version': version, 'Count': count})
        # print(version)

