import csv
import requests
import statistics

def extract_contract_code(contract_address):
    # Build the Etherscan API URL for the contract creation code
    etherscan_api_url = "https://api.etherscan.io/api"
    etherscan_api_key = "6XGT5XNWW6FFG6PVFARUY79JHWIYJV9XJZ"
    api_params = {
        "module": "proxy",
        "action": "eth_getCode",
        "address": contract_address,
        "tag": "latest",
        "apikey": etherscan_api_key
    }
    response = requests.get(etherscan_api_url, params=api_params)
    if response.status_code == 200:
        # Extract the contract creation code from the API response
        result = response.json().get("result")
        if result is not None:
            return result[2:]  # Remove the "0x" prefix from the hex string
        else:
            return None
    else:
        # Handle the API error
        print(f"Error: {response.status_code} - {response.text}")
        return None


# Read the contract addresses from the CSV file
contract_addresses = []
with open("contract.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        contract_addresses.append(row[0])

# Extract the contract creation code for each contract address and store the code length in a list
code_lengths = []
for contract_address in contract_addresses:
    contract_code = extract_contract_code(contract_address)
    if contract_code is not None:
        code_length = len(contract_code)
        code_lengths.append(code_length)

        print(f"Contract address: {contract_address}")
        numeric_count = sum(c.isdigit() for c in contract_code)
        non_numeric_count = code_length - numeric_count
        print(f"Contract creation code size: {code_length} characters")
        print("=" * 80)

        # Add the code_length to the CSV file
        with open("bytecode_length.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([code_length])

# Calculate and print the statistics of the list of code lengths
if len(code_lengths) > 0:
    avg = statistics.mean(code_lengths)
    var = statistics.variance(code_lengths)
    med = statistics.median(code_lengths)
    std = statistics.stdev(code_lengths)
    min_len = min(code_lengths)
    max_len = max(code_lengths)

    print(f"\nAverage code length: {avg}")
    print(f"Variance of code length: {var}")
    print(f"Median code length: {med}")
    print(f"Standard deviation of code length: {std}")
    print(f"Minimum code length: {min_len}")
    print(f"Maximum code length: {max_len}")
else:
    print("No valid code lengths found.")
