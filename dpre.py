import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import argparse

# Load the dataset
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--file_path', required=True, help='The path to the dataset file.')
  args = parser.parse_args()
  data = pd.read_csv(args.file_path)

# Data Cleaning
# Task 1: Remove rows with missing values
data = data.dropna()

# Task 2: Replace any negative or zero values in 'item_price' and 'transaction_amount' with NaN
data['item_price'] = data['item_price'].apply(lambda x: x if x > 0 else np.nan)
data['transaction_amount'] = data['transaction_amount'].apply(lambda x: x if x > 0 else np.nan)

# Data Transformation
# Task 1: Convert 'date' to datetime format (update the date format)
data['date'] = pd.to_datetime(data['date'], format='%m/%d/%Y')

# Task 2: Encode categorical variables using label encoding
label_encoder = LabelEncoder()
data['item_name'] = label_encoder.fit_transform(data['item_name'])
data['item_type'] = label_encoder.fit_transform(data['item_type'])  # Fixed the missing period here
data['transaction_type'] = label_encoder.fit_transform(data['transaction_type'])
data['received_by'] = label_encoder.fit_transform(data['received_by'])
data['time_of_sale'] = label_encoder.fit_transform(data['time_of_sale'])

# Data Reduction
# Task 1: Drop unnecessary columns
data = data.drop(['order_id'], axis=1)

# Task 2: Reduce the granularity of 'item_price' by binning it into categories
bins = [0, 25, 50, 100, float('inf')]
labels = ['Low', 'Medium', 'High', 'Very High']
data['item_price_category'] = pd.cut(data['item_price'], bins=bins, labels=labels)

# Save the resulting dataframe as a new CSV file
data.to_csv("res_dpre.csv", index=False)