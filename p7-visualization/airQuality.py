import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better aesthetics

sns.set_style("whitegrid")

# Load the Air Quality dataset

# Replace 'AirQualityUCI.csv' with the actual file path

# Note: UCI dataset uses ; separator and , for decimals

df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')

# Basic data cleaning for visualization

# Remove rows with invalid values (e.g., CO(GT) = -200)

df = df[df['CO(GT)'] != -200]

# Convert Date to datetime

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Display first few rows to understand the dataset

print("Dataset Preview:")
print(df.head())
print("\n")

# Plot 1: Line Plot - CO(GT) over Time

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['CO(GT)'], color='blue', label='CO(GT)')
plt.title('CO Concentration Over Time')
plt.xlabel('Date')
plt.ylabel('CO(GT) (mg/m³)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Box Plot - CO(GT) by Month

df['Month'] = df['Date'].dt.month
plt.figure(figsize=(10, 6))
sns.boxplot(x='Month', y='CO(GT)', data=df, palette='Blues')
plt.title('CO Concentration Distribution by Month')
plt.xlabel('Month')
plt.ylabel('CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()

# Plot 3: Scatter Plot - CO(GT) vs NO2(GT)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='NO2(GT)', y='CO(GT)', data=df, hue='T', size='T', palette='coolwarm')
plt.title('CO vs NO2 Concentration (Colored by Temperature)')
plt.xlabel('NO2(GT) (µg/m³)')
plt.ylabel('CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()

# Plot 4: Heatmap - Correlation Matrix

plt.figure(figsize=(10, 6))

# Select numerical columns for correlation

numerical_cols = ['CO(GT)', 'NO2(GT)', 'NOx(GT)', 'T', 'RH', 'AH']
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Air Quality Features')
plt.tight_layout()
plt.show()

# Plot 5: Bar Plot - Average CO(GT) by Hour

df['Hour'] = pd.to_datetime(df['Time'], format='%H.%M.%S').dt.hour
plt.figure(figsize=(10, 6))
sns.barplot(x='Hour', y='CO(GT)', data=df, palette='viridis')
plt.title('Average CO Concentration by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average CO(GT) (mg/m³)')
plt.tight_layout()
plt.show()
