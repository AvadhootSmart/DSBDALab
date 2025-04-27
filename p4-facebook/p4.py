import pandas as pd

# Load the Facebook Metrics dataset
# Replace 'dataset_Facebook.csv' with the actual file path
df = pd.read_csv('dataset_Facebook.csv')

# Display first few rows to understand the dataset
print("Original Dataset Preview:")
print(df.head())
print("\n")

# a. Create data subsets
# Subset 1: Select specific columns (e.g., 'Page total likes', 'Type', 'Post Month')
subset1 = df[['Page total likes', 'Type', 'Post Month']]
print("Subset 1 (Selected Columns):")
print(subset1.head())
print("\n")

# Subset 2: Filter rows (e.g., posts with Type='Photo')
subset2 = df[df['Type'] == 'Photo']
print("Subset 2 (Photo Posts Only):")
print(subset2.head())
print("\n")

# b. Merge Data
# Create two subsets for merging
subset3 = df[['Page total likes', 'Post Month']].iloc[:50]  # First 50 rows
subset4 = df[['Post Month', 'Lifetime Post Total Reach']].iloc[:50]  # First 50 rows
merged_df = pd.merge(subset3, subset4, on='Post Month', how='inner')
print("Merged Data (on Post Month):")
print(merged_df.head())
print("\n")

# c. Sort Data
# Sort by 'Lifetime Post Total Reach' in descending order
sorted_df = df.sort_values(by='Lifetime Post Total Reach', ascending=False)
print("Sorted Data (by Lifetime Post Total Reach):")
print(sorted_df[['Page total likes', 'Type', 'Lifetime Post Total Reach']].head())
print("\n")

# d. Transpose Data
# Transpose the dataset (rows become columns, columns become rows)
transposed_df = df.transpose()
print("Transposed Data:")
print(transposed_df.head())
print("\n")

# e. Shape and Reshape Data
# Display the shape of the dataset
print("Dataset Shape (Rows, Columns):", df.shape)
print("\n")

# Reshape using pivot (e.g., average 'Lifetime Post Total Reach' by 'Post Month' and 'Type')
reshaped_df = df.pivot_table(index='Post Month', 
                             columns='Type', 
                             values='Lifetime Post Total Reach', 
                             aggfunc='mean')
print("Reshaped Data (Pivot Table - Avg Reach by Month and Type):")
print(reshaped_df.head())
print("\n")
