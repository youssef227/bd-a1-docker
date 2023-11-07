import pandas as pd
from sklearn.cluster import KMeans
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--file_path', required=True, help='The path to the dataset file.')
  args = parser.parse_args()
# Load the dataset
  data = pd.read_csv(args.file_path)

# Select the columns you want to use for clustering (for example, 'item_price' and 'quantity')
# You can modify this based on your dataset
selected_columns = data[['item_price', 'quantity']]

# Create a K-means model with k=3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the model to the selected columns
kmeans.fit(selected_columns)

# Predict cluster labels for each record
cluster_labels = kmeans.predict(selected_columns)

# Count the number of records in each cluster
cluster_counts = pd.Series(cluster_labels).value_counts()



# Save the cluster counts to a text file
cluster_counts.to_csv('k.txt', sep='\t', header=['Cluster Count'], index_label='Cluster')