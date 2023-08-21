import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file (assuming balance values are in a column called 'balance')
df = pd.read_csv('balance.csv')
data = df['balance'].values

# Calculate CCDF values
ccdf = 1 - np.cumsum(np.ones_like(data))/len(data)

# Sort data
data_sorted = np.sort(data)

# Plot the graph
plt.loglog(data_sorted, ccdf, 'bo', markersize=3)
plt.xlabel('Balance in Ethereum per contract',fontsize=15)
plt.ylabel('CCDF',fontsize=16)
plt.title('Distribution of Ethereum balances per contract',fontsize=16)
plt.show()
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)

