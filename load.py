import argparse
import pandas as pd

def load_dataset(file_path):
  """Loads a dataset from a CSV file.

  Args:
    file_path: The path to the CSV file.

  Returns:
    A Pandas DataFrame containing the dataset.
  """

  df = pd.read_csv(file_path)
  return df

def print_head(df):
  """Prints the head of a Pandas DataFrame.

  Args:
    df: A Pandas DataFrame.
  """

  print(df.head())

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--file_path', required=True, help='The path to the dataset file.')
  args = parser.parse_args()

  df = load_dataset(args.file_path)
  print_head(df)
