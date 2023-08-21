# SC1-Emperical-Study-Group6
address_to_json.py - It fetches the sol files of contract from etherscan using the public address of contracts present in contract.csv.


json_to_sol.py - It converts the json files to sol files.

versionfinder.py- It finds alll of the compiler version that are used in json files and store in two files
1. version.csv(Contains only Count)
2. version2.csv(Contains version Name, Count)

contract_name_count_pair.py - It finds the name of contract and coount from the json file and store in a txt file and csv file stores just the count.

expression2.py- It uses version2.csv and removes unnecessary characters from version and stores in version3.csv

expression_editor2.py - It calculates the counts of all the version and stores in verson4.csv

graph.py - It uses version4.csv to plot a bar graph.

bytecode_length_finder_for_csv.py - It uses contract.csv and produces bytecode length of respective contract and store in bytecode_length.csv
It also produces statistics(avg,var,median,std deviation,min,max) on screen.

bytecode_length_stats finder.py - It uses bytecode_length.csv and store the statistics in bytecode_length_stats.txt

balance.csv and transaction.csv are fetched from googlebigquery by writing queries for balance and transaction respectively.
CCDF_balance.py-It uses balance.csv file to produce Complementary Cumulative Distribution Function(CCDF) graph based on balance.
CCDF_transaction.py- It uses transactio.csv to produce CCDF graph based on transations.

lines_statistics- It uses all the sol file to calculate code_lines, comment_lines, total_lines, comment_ratio and
store it in code_lines.csv, comment_lines.csv, total_lines.csv, comment_ratio.csv respectively.
statistics_finder.py - It produces the (avg,var,std deviation,min,max) of above values.

correlation_matrix_generator.py- It combines all the csv file(Bytecode_length, code_lines, comment_lines,comment_ratio, contract_count,total_lines,trasaction) into a singhle excel sheet,
on which we find the correlation betwwn parameters by applying the correlation formula(=correl(parameter1_start:parameter1_end,parameter2_start:parameter2_end)

graph_plotter_bytecode.py- It creates the histogram for bytecodes length.
graph_plotter_codelines.py- It creates the histogram for code lines.
graph_plotter_ndc.py- It produces histogram for Number of contract declared in the source code.

ndc-ndf_statistics.py- It count the ndc(no. of declared contracts), ndf(no. of declared function) and store 
in contract_count_ndc.csv, function_count_ndf.csv respectively.

ndc_statistics.py- It generates the  statistics(avg,var,median,std deviation,min,max) from contract_count_ndc and store in ndc.txt
ndf_statistics.py- It generates the  statistics(avg,var,median,std deviation,min,max)  from function_count_ndf and store in ndf.txt

top10_finder.py -It finds the top 10 contracts based on count and store inside top_10_conract_counts.txt





