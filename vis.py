import pandas as pd
import matplotlib.pyplot as plt
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--file_path', required=True, help='The path to the dataset file.')
  args = parser.parse_args()
# Load the dataset
  data = pd.read_csv(args.file_path)

# Group the data by 'item_type' and calculate the sum of 'transaction_amount' for each item type
item_type_total = data.groupby('item_type')['transaction_amount'].sum()

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(item_type_total.index, item_type_total.values)
plt.xlabel('Item Type')
plt.ylabel('Total Transaction Amount')
plt.title('Total Transaction Amount by Item Type')

# Save the visualization as "vis.png"
plt.savefig('vis.png')

# Show the plot (optional)
plt.show()