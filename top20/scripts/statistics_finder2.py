import os
import concurrent.futures
import statistics


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


def analyze_file(file_path):
    try:
        code_lines, comment_lines = count_lines_of_code(file_path)
        total_lines = code_lines + comment_lines
        if total_lines > 0:
            comment_ratio = round(comment_lines / code_lines * 100, 2)
        else:
            comment_ratio = 0
        with open(file_path, 'r') as f:
            num_lines = sum(1 for line in f if line.strip())
        return file_path, code_lines, comment_lines, comment_ratio, total_lines
    except:
        print(f'Error processing file: {file_path}')
        return file_path, 0, 0, 0, 0


def analyze_directory(directory_path):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                if file_name.endswith('.sol'):
                    file_path = os.path.join(root, file_name)
                    results.append(executor.submit(analyze_file, file_path))
    return [r.result() for r in results]


if __name__ == '__main__':
    results = analyze_directory('./top20sol')
    for file_name, code_lines, comment_lines, comment_ratio, total_lines in results:
        print(f'{file_name}: Code lines: {code_lines}, Comment lines: {comment_lines}, Comment ratio: {comment_ratio}%, Total lines: {total_lines}')
