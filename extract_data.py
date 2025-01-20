import re
import argparse
import os

input_file = 'test_results.txt'
timing_file = 'timing.txt'

def round_float_in_data(text):
    return re.sub(r'(\d+\.\d+)', lambda x: f"{float(x.group(1)):.2f}", text)

def process_results(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    runs = re.findall(r'(Run (\d+) for query (\d+))\n(.*?)Completed run \d+ for query \d+', content, re.DOTALL)

    with open(timing_file, 'a') as timing_out:
        for run in runs:
            run_header, run_number, query_number, run_data = run

            table_match = re.search(r'(\+[-+]+\+.*?)\d+ tuples', run_data, re.DOTALL)
            # print(table_match.group(1))
            if table_match:
                table_data = table_match.group(1)

                table_lines = table_data.splitlines()
                header = [col.strip() for col in table_lines[1].split('|') if col.strip()]
                formatted_rows = []
                for line in table_lines[3:-1]: 
                    columns = [col.strip() for col in line.split('|') if col.strip()]
                    # print(columns)
                    rounded_columns = [round_float_in_data(col) for col in columns]
                    formatted_rows.append('|'.join(rounded_columns))

                cwd = os.getcwd();
                op_path = os.path.join(cwd,'output_monet')
                if not os.path.exists(op_path):
                    os.makedirs(op_path)
                output_file = f'{op_path}/q{query_number}.out'
                with open(output_file, 'w') as table_out:
                    table_out.write('|'.join(header) + '\n')
                    table_out.write('\n'.join(formatted_rows))

            timing_info = re.search(r'real\s+([^\n]+)\nuser\s+([^\n]+)\nsys\s+([^\n]+)', run_data)
            if timing_info:
                real_time, user_time, sys_time = timing_info.groups()
                timing_out.write(f'Run {run_number} for query {query_number}\n')
                timing_out.write(f'real: {real_time}\nuser: {user_time}\nsys: {sys_time}\n\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract table data")
    parser.add_argument('--input_file', default='test_results.txt', help='The input file to process.')

    args = parser.parse_args()
    process_results(args.input_file)