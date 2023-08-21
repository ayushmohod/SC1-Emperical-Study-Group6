import os

# function to calculate the number of lines of code in a given function
def count_lines_of_code(function_code):
    code_lines = function_code.split("\n")
    num_lines = len(code_lines)
    return num_lines

# function to read a .sol file and return the contract code as a string
def read_contract_file(filepath):
    with open(filepath, "r") as f:
        contract_code = f.read()
    return contract_code

# function to parse the contract code and return a dictionary of functions and their code
def parse_contract_code(contract_code):
    function_code_dict = {}
    contract_lines = contract_code.split("\n")
    current_function_code = ""
    current_function_name = ""
    for line in contract_lines:
        if "function " in line:
            # save the previous function's code, if any
            if current_function_name != "":
                function_code_dict[current_function_name] = current_function_code.strip()
            # start a new function
            current_function_code = line + "\n"
            current_function_name = line.split("function ")[1].split("(")[0]
        else:
            # add the line to the current function's code
            current_function_code += line + "\n"
    # save the last function's code
    if current_function_name != "":
        function_code_dict[current_function_name] = current_function_code.strip()
    return function_code_dict

# function to calculate the average number of lines of code per function
def calculate_average_lines_per_function(function_code_dict):
    num_functions = len(function_code_dict)
    total_lines = 0
    for function_name, function_code in function_code_dict.items():
        lines_in_function = count_lines_of_code(function_code)
        total_lines += lines_in_function
    if num_functions > 0:
        average_lines_per_function = total_lines / num_functions
    else:
        average_lines_per_function = 0
    return average_lines_per_function

# main function to scan all .sol files in a folder and calculate the average number of lines of code per function for each file
def main(folderpath):
    for filename in os.listdir(folderpath):
        if filename.endswith(".sol"):
            filepath = os.path.join(folderpath, filename)
            contract_code = read_contract_file(filepath)
            function_code_dict = parse_contract_code(contract_code)
            average_lines_per_function = calculate_average_lines_per_function(function_code_dict)
            print(f"{filename}: Average number of lines of code per function: {average_lines_per_function}")
import csv

# main function to scan all .sol files in a folder and calculate the average number of lines of code per function for each file
def main(folderpath):
    with open("lpc.csv", "w", newline="") as csvfile:
        fieldnames = ["Filename", "Average Lines of Code per Function"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for filename in os.listdir(folderpath):
            if filename.endswith(".sol"):
                filepath = os.path.join(folderpath, filename)
                contract_code = read_contract_file(filepath)
                function_code_dict = parse_contract_code(contract_code)
                average_lines_per_function = calculate_average_lines_per_function(function_code_dict)
                writer.writerow({"Filename": filename, "Average Lines of Code per Function": average_lines_per_function})

# example usage
if __name__ == "__main__":
    folderpath = "top20sol" # replace with the path of the folder containing the .sol files
    main(folderpath)

