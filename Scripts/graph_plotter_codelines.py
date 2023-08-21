# import pandas as pd
# import matplotlib.pyplot as plt

# # read CSV file into a pandas dataframe
# # df = pd.read_csv('filename.csv')
# df = pd.read_csv('./matrix_data/code_lines.csv')

# # create a histogram of the values in the column you want to graph
# plt.hist(df['Code Lines'], bins=range(min(df['Code Lines']), max(df['Code Lines']) + 100, 100))

# # set the title and axis labels
# plt.title('Histogram')
# plt.xlabel('X Axis Label')
# plt.ylabel('Y Axis Label')

# # display the graph
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# read CSV file into a pandas dataframe
# df = pd.read_csv('filename.csv')
df = pd.read_csv('./matrix_data/code_lines.csv')

# create a histogram of the values in the column you want to graph
plt.hist(df['Code Lines'], bins=range(min(df['Code Lines']), max(df['Code Lines']) + 100, 100), edgecolor='black')

# set the title and axis labels
plt.title('Histogram')
plt.xlabel('Code Total Lines', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)

# display the graph
plt.show()
