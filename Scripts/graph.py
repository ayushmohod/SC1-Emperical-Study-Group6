# import matplotlib.pyplot as plt


# # data = {'v0.4.0': 3, 'v0.4.1': 0, 'v0.4.2': 4, 'v0.4.3': 0, 'v0.4.4': 7, 'v0.4.5': 1, 'v0.4.6': 9, 'v0.4.7': 1, 'v0.4.8': 32, 'v0.4.9': 12, 'v0.4.10': 15, 'v0.4.11': 249, 'v0.4.12': 34, 'v0.4.13': 143, 'v0.4.14': 32, 'v0.4.15': 160, 'v0.4.16': 284, 'v0.4.17': 132, 'v0.4.18': 916, 'v0.4.19': 928, 'v0.4.20': 312, 'v0.4.21': 818, 'v0.4.22': 77, 'v0.4.23': 499, 'v0.4.24': 2556, 'v0.4.25': 1513, 'v0.4.26': 113, 'v0.5.0': 2, 'v0.5.1': 1, 'v0.5.2': 0, 'v0.5.3': 0, 'v0.5.4': 0, 'v0.5.5': 0, 'v0.5.6': 0, 'v0.5.7': 0, 'v0.5.8': 3, 'v0.5.9': 0, 'v0.5.10': 1, 'v0.5.11': 3, 'v0.5.12': 0, 'v0.5.13': 0, 'v0.5.14': 0, 'v0.5.15': 0, 'v0.5.16': 0, 'v0.5.17': 0}
# data = {'v0.4.4': 7, 'v0.4.5': 1, 'v0.4.6': 9, 'v0.4.7': 1, 'v0.4.8': 32, 'v0.4.9': 12, 'v0.4.10': 15, 'v0.4.11': 249, 'v0.4.12': 34, 'v0.4.13': 143, 'v0.4.14': 32, 'v0.4.15': 160, 'v0.4.16': 284, 'v0.4.17': 132, 'v0.4.18': 916, 'v0.4.19': 928, 'v0.4.20': 312, 'v0.4.21': 818, 'v0.4.22': 77, 'v0.4.23': 499, 'v0.4.24': 2556, 'v0.4.25': 1513, 'v0.4.26': 113}

# names = list(data.keys())
# values = list(data.values())

# plt.bar(names, values)
# plt.xticks(rotation=60)
# plt.tick_params(axis='x', labelsize=15)

# plt.show()
# for name, value in zip(names, values):
#     plt.text(name, value, str(value), ha='center', va='bottom')
# for name, value in zip(names, values):
#     plt.text(name, value, str(value), ha='center', va='bottom', fontdict={'fontsize': 5})



import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a pandas DataFrame and sort by Version column in ascending order
df = pd.read_csv('version4.csv').sort_values('Version')

# Extract data from DataFrame
x = df['Version']
y = df['Count']

# Plot data as a bar graph
plt.bar(x, y)

# Add axis labels and title
plt.xlabel('Version')
plt.ylabel('Count')
plt.title('Count of Different Versions')
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
# Rotate x-axis labels by 90 degrees
plt.xticks(rotation=60)

# Show plot
plt.show()

