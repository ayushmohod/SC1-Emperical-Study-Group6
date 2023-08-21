# import csv

# # open the input CSV file
# with open('version3.csv', 'r') as infile:
#     reader = csv.reader(infile)
#     # skip the header row
#     next(reader)
#     # create a dictionary to store the sum of values for each key
#     sums = {}
#     # iterate over each row in the input CSV file
#     for row in reader:
#         # assume the first column contains the key and the second column contains the value
#         key = row[0]
#         value = int(row[1])
#         # add the value to the sum for this key
#         if key in sums:
#             sums[key] += value
#         else:
#             sums[key] = value

# # open the output CSV file
# with open('version4.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile)
#     # iterate over the keys in the dictionary and write each key-value pair to a new row in the output CSV file
#     for key, value in sums.items():
#         writer.writerow([key, value])


import csv

# open the input CSV file

with open('version3.csv', 'r') as infile:
    reader = csv.reader(infile)
    # read the header row
    header = next(reader)
    # create a dictionary to store the sum of values for each key
    sums = {}
    # iterate over each row in the input CSV file
    for row in reader:
    # assume the first column contains the key and the second column contains the value
        key = row[0]
        value = int(row[1])
        # add the value to the sum for this key
        if key in sums:
            sums[key] += value
        else:
            sums[key] = value

# open the output CSV file

with open('version4.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    # write the header row to the output CSV file
    writer.writerow(header)
    # iterate over the keys in the dictionary and write each key-value pair to a new row in the output CSV file
    for key, value in sums.items():
        writer.writerow([key, value])