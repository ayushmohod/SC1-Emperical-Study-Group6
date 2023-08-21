import os
import concurrent.futures
import statistics
import csv


def count_lines_of_code(file_path):
    with open(file_path, 'r') as f:
        code_lines = 0
        comment_lines = 0
        in_comment = False
        for line in f:
            line = line.strip()
            if not line or line.startswith('//'):  # skip empty or single-line comment lines
                comment_lines += 1
                continue
            if in_comment:  # skip multi-line comment lines until the closing symbol
                if '*/' in line:
                    line = line.split('*/', 1)[1]
                    in_comment = False
                else:
                    comment_lines += 1
                    continue
            if line.startswith('/*'):  # skip the opening symbol of multi-line comments
                if '*/' not in line:
                    in_comment = True
            else:
                code_lines += 1
    return code_lines, comment_lines


def analyze_file(file_path, code_lines_list, comment_lines_list, comment_ratio_list,total_lines_list):
    try:
        code_lines, comment_lines = count_lines_of_code(file_path)
        total_lines = code_lines + comment_lines
        if total_lines > 0:
            comment_ratio = round(comment_lines / code_lines * 100, 2)
        else:
            comment_ratio = 0
        with open(file_path, 'r') as f:
            num_lines = sum(1 for line in f if line.strip())
        code_lines_list.append(code_lines)
        comment_lines_list.append(comment_lines)
        comment_ratio_list.append(comment_ratio)
        total_lines_list.append(total_lines)
    except:
        print(f'Error processing file: {file_path}')


# def analyze_directory(directory_path):
#     code_lines_list = []
#     comment_lines_list = []
#     comment_ratio_list = []
#     total_lines_list=[]
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         for root, _, files in os.walk(directory_path):
#             for file_name in files:
#                 if file_name.endswith('.sol'):
#                     file_path = os.path.join(root, file_name)
#                     executor.submit(analyze_file, file_path, code_lines_list, comment_lines_list, comment_ratio_list,total_lines_list)
#     print(code_lines_list)
#     return code_lines_list, comment_lines_list, comment_ratio_list,total_lines_list
def analyze_directory(directory_path):
    code_lines_list = []
    comment_lines_list = []
    comment_ratio_list = []
    total_lines_list=[]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                if file_name.endswith('.sol'):
                    file_path = os.path.join(root, file_name)
                    executor.submit(analyze_file, file_path, code_lines_list, comment_lines_list, comment_ratio_list, total_lines_list)

    with open('./matrix_data/total_lines.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Total Lines'])
        for line in total_lines_list:
            writer.writerow([line])
    with open('./matrix_data/code_lines.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Code Lines'])
        for line in code_lines_list:
            writer.writerow([line])
    with open('./matrix_data/comment_ratio.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Comment Ratio'])
        for line in comment_ratio_list:
            writer.writerow([line])
    with open('./matrix_data/comment_lines.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Comment Lines'])
        for line in comment_lines_list:
            writer.writerow([line])
    

    return code_lines_list, comment_lines_list, comment_ratio_list, total_lines_list



if __name__ == '__main__':
    code_lines, comment_lines, comment_ratio, total_lines = analyze_directory('./Smart_Contracts')
    
    
    # code_lines_avg = statistics.mean(code_lines)
    # code_lines_var = statistics.variance(code_lines)
    # code_lines_std = statistics.stdev(code_lines)
    # code_lines_min = min(code_lines)
    # code_lines_max = max(code_lines)

    # comment_lines_avg = statistics.mean(comment_lines)
    # comment_lines_var = statistics.variance(comment_lines)
    # comment_lines_std = statistics.stdev(comment_lines)
    # comment_lines_min = min(comment_lines)
    # comment_lines_max = max(comment_lines)

    # total_lines_avg = statistics.mean(total_lines)
    # total_lines_var = statistics.variance(total_lines)
    # total_lines_std = statistics.stdev(total_lines)
    # total_lines_min = min(total_lines)
    # total_lines_max = max(total_lines)

    # comment_ratio_avg = statistics.mean(comment_ratio)
    # comment_ratio_var = statistics.variance(comment_ratio)
    # comment_ratio_std = statistics.stdev(comment_ratio)
    # comment_ratio_min = min(comment_ratio)
    # comment_ratio_max = max(comment_ratio)

    # print(f'Code lines: average={code_lines_avg}, variance={code_lines_var}, '
    #       f'standard deviation={code_lines_std}, min={code_lines_min}, max={code_lines_max}')
    
    # print(f'Total lines: average={total_lines_avg}, variance={total_lines_var}, '
    #       f'standard deviation={total_lines_std}, min={total_lines_min}, max={total_lines_max}')
    
    # print(f'Comment lines: average={comment_lines_avg}, variance={comment_lines_var}, '
    #       f'standard deviation={comment_lines_std}, min={comment_lines_min}, max={comment_lines_max}')
    
    # print(f'Comment Ratio: average={comment_ratio_avg}, variance={comment_ratio_var}, '
    #       f'standard deviation={comment_ratio_std}, min={comment_ratio_min}, max={comment_ratio_max}')
    

    # print(f'Comment lines: average={comment_lines_avg}, variance={comment_lines_var}, '
    #       f'st
if __name__ == '__main__':
    analyze_directory('./Smart_Contracts')
    
