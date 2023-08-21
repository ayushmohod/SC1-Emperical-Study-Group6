import os
import re
import csv


def count_contracts_and_functions(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        # Remove single-line comments (// ...)
        content = re.sub(r'\/\/[^\n]*', '', content)
        # Remove multi-line comments (/* ... */)
        content = re.sub(r'\/\*[\s\S]*?\*\/', '', content)
        # Count occurrences of "contract" keyword
        num_contracts = content.count('contract')
        # Count occurrences of "function" keyword
        num_functions = content.count('function')
        return num_contracts, num_functions


def count_contracts_and_functions_in_directory(directory):
    results = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.sol'):
            file_path = os.path.join(directory, file_name)
            num_contracts, num_functions = count_contracts_and_functions(file_path)
            results[file_name] = {'contracts': num_contracts, 'functions': num_functions}
    return results


results = count_contracts_and_functions_in_directory('./Smart_Contracts')
for file_name, counts in results.items():
    print(f"{file_name}: contracts={counts['contracts']}, functions={counts['functions']}")

with open('./matrix_data/contract_count_ndc.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Contracts'])
    for file_name, counts in results.items():
        writer.writerow([counts['contracts'],])

with open('./matrix_data/function_count_ndf.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Functions'])
    for file_name, counts in results.items():
        writer.writerow([counts['functions']])

# with open("function_counts_for_ndf", "w") as file:
#     for contract, count in results:
#         file.write(f"{contract}: {count}\n")
    
    
   
