import pandas as pd
import sys
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--file_path', required=True, help='The path to the dataset file.')
  args = parser.parse_args()
  data = pd.read_csv(args.file_path)


summary_stats = data.describe()
summary_stats.to_csv('eda-in-1.txt', sep='\t')


with open('eda-in-2.txt', 'w') as file, sys.stdout as original_stdout:
    sys.stdout = file
    data.info()
    sys.stdout = original_stdout


unique_values = {}
categorical_columns = data.select_dtypes(include=['object']).columns
for column in categorical_columns:
    unique_values[column] = data[column].nunique()
with open('eda-in-3.txt', 'w') as file:
    for column, unique_count in unique_values.items():
        file.write(f'Column: {column}, Unique Values: {unique_count}\n')