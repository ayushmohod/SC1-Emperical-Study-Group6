import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('bytecode_length.csv', header=None, names=['data'])

# Get the minimum value
min_value = df['data'].min()

# Get the maximum value
max_value = df['data'].max()

# Get the mean value
mean_value = df['data'].mean()

# Get the median value
median_value = df['data'].median()

# Get the standard deviation value
std_value = df['data'].std()

# Get the variance value
var_value = df['data'].var()

with open('bytecode_length_stats.txt', 'w') as f:
    f.write("Minimum value: {}\n".format(min_value))
    f.write("Maximum value: {}\n".format(max_value))
    f.write("Mean value: {}\n".format(mean_value))
    f.write("Median value: {}\n".format(median_value))
    f.write("Standard deviation: {}\n".format(std_value))
    f.write("Variance value: {}\n".format(var_value))

# Print the results
print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Mean value:", mean_value)
print("Median value:", median_value)
print("Standard deviation:", std_value)
print("Variance value:", var_value)
