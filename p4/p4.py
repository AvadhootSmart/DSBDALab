import pandas as pd

# Load dataset
df = pd.read_csv('facebook_metrics.csv')  # Replace with actual file path

# a. Create data subsets
subset1 = df[['Page total likes', 'Post Month']]  # Select specific columns
subset2 = df[df['Post Month'] == 12]  # Filter rows (e.g., December posts)
print("Subset 1:\n", subset1.head())
print("Subset 2:\n", subset2.head())

# b. Merge data (create two subsets and merge)
subset3 = df[['Page total likes', 'Post Month']].iloc[:50]
subset4 = df[['Post Month', 'Lifetime Post Total Reach']].iloc[:50]
merged_df = pd.merge(subset3, subset4, on='Post Month', how='inner')
print("Merged Data:\n", merged_df.head())

# c. Sort data
sorted_df = df.sort_values(by='Lifetime Post Total Reach', ascending=False)
print("Sorted Data:\n", sorted_df.head())

# d. Transpose data
transposed_df = df.transpose()
print("Transposed Data:\n", transposed_df.head())

# e. Shape and reshape data
print("Shape:", df.shape)  # Rows, Columns
# Reshape using pivot (example: pivot by Post Month and Type)
reshaped_df = df.pivot_table(index='Post Month', columns='Type', values='Lifetime Post Total Reach', aggfunc='mean')
print("Reshaped Data:\n", reshaped_df.head())
