import pandas as pd
import os

# set the input directory and output file name
input_dir = './matrix_data'
output_file = 'correlation_matrix.xlsx'

# create an empty list to store the DataFrames
dfs = []

# loop through the CSV files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):
        # read CSV file
        file_path = os.path.join(input_dir, file_name)
        df = pd.read_csv(file_path)
        
        # add the DataFrame to the list
        dfs.append(df)

# concatenate the DataFrames into a single DataFrame
combined_df = pd.concat(dfs, axis=1)

# export to Excel file
writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
combined_df.to_excel(writer, sheet_name='Sheet1', startrow=0, index=False)

# save and close the Excel file
writer.save()
